import pyautogui
import sounddevice as sd
import numpy as np
import pyttsx3

# Set the clap detection threshold
CLAP_THRESHOLD = 15
clap_detected = False

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def detect_clap(indata, frames, time, status):
    """Detect claps based on audio input."""
    global clap_detected

    # Calculate the normalized volume
    volume_norm = np.linalg.norm(indata) * 10

    if volume_norm > CLAP_THRESHOLD:
        print("Clap detected!")
        clap_detected = True  # Set flag when clap is detected

def listen_for_claps():
    """Listen for claps using the audio input stream."""
    with sd.InputStream(callback=detect_clap):
        sd.sleep(100)  # Poll every 100ms for better responsiveness

def when_i_clap_write():
    """Process the clap detection and execute the corresponding key press."""
    global clap_detected

    while True:

        with open("input.txt", "r") as myfile:
            command = myfile.read()
        if "if I clap type" in command:
            key = command.replace("if I clap type", "").strip()

            
            listen_for_claps()  # Check for claps
            if clap_detected:
                pyautogui.write(key)  # Press the key
                print(f"Wrote: {key}")
                clap_detected = False  # Reset the flag

while True:
    when_i_clap_write()