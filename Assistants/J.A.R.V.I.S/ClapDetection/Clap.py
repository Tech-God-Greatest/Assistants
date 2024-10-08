import sounddevice as sd
import numpy as np
import pyttsx3

threshold = 20
Clap = False

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def detect_clap(indata,frames,time,status):
    global Clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm>threshold:
        print("Clapped!")
        Clap = True

def Listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)
    
def MainClapExe():
    global Clap
    while True:
        Listen_for_claps()
        if Clap==True:
            with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "w") as file:
                file.write("1")
                print("Jarvis activated! Ready to serve you sir. What's your command?")
                speak("Jarvis activated! Ready to serve you sir. What's your command?")
            Clap = False
                
        else:
            pass

while True:
    MainClapExe()