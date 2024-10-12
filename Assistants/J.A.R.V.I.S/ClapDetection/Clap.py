import sounddevice as sd
import numpy as np
import pyttsx3

# Set the clap detection threshold
CLAP_THRESHOLD = 20
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
        clap_detected = True

def listen_for_claps():
    """Listen for claps using the audio input stream."""

    with sd.InputStream(callback=detect_clap):
        sd.sleep(1000)

def main_clap_exe():
    """Main loop to check for clap and change state."""

    global clap_detected

    while True:
        # Read the current state from the state file

        with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "r") as state_file:
            state = state_file.read().strip()
        
        # If state is "0", listen for claps
        if state == "0":

            listen_for_claps()

            if clap_detected:
                # Change state to "1" when a clap is detected

                with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "w") as file:
                    
                    file.write("1")

                    print("Jarvis activated! Ready to serve you, sir. What's your command?")
                    speak("Jarvis activated! Ready to serve you, sir. What's your command?")
                
                # Reset the clap detection flag
                clap_detected = False

# Start the clap detection loop
if __name__ == "__main__":

    main_clap_exe()