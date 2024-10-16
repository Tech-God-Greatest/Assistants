
import time
import threading
import subprocess
import pyttsx3
from groq import Groq
import pyautogui
from time import sleep
from Automation.Web_Open import openweb
from Automation.App_Open import openapp
from Image_Generation.image_generator import generateimage
from Youtube.Open_Youtube import play_music
from Youtube.Open_Youtube import play_video
from Automation.scroll import perform_scroll_action
from Automation.tab import perform_browser_action
from Presentation.AIpresentation import generateppt
from Youtube.Yt_Controls import perform_media_action
from Features.Write import write
from Features.Press import press
from Features.Create_Files import create_file
from Features.Find_IP import find_my_ip
from Features.Set_BR import set_brightness_windows
from Features.Set_Get_Volume import set_volume_windows
from Time_Operations.Timer import set_timer

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("step 1 completed")

with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "w") as file:
    file.write("0")

with open("input.txt", "w") as file:
    file.write("")

with open("output.txt", "w") as file:
    file.write("")

subprocess.Popen(["python", "D:\\Assistants\\J.A.R.V.I.S\\STT.py"])
subprocess.Popen(["python", "D:\\Assistants\\J.A.R.V.I.S\\ClapDetection\\Clap.py"])
subprocess.Popen(["python", "D:\\Assistants\\J.A.R.V.I.S\\ClapDetection\\Clap_To.py"])
subprocess.Popen(["python", "D:\\Assistants\\J.A.R.V.I.S\\ClapDetection\\Clap_To_write.py"])

time.sleep(4)

subprocess.Popen(["python", "D:\\Assistants\\J.A.R.V.I.S\\UI\\UI.py"])

time.sleep(5)

speak("step 2 completed")

client = Groq(api_key="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")
Checker = ""



conversation_history = [
    {
        "role": "system",
        "content": "You are J.A.R.V.I.S from the Iron Man movies, your inventor and user is Lakshit Agarwal. Keep responses small and like J.A.R.V.I.S. If any command related to claps are given say 'Sure sir, waiting for claps.'"
    }
]

speak("started")

def shutdown(Text):
    if "shutdown" in Text:
        with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "w") as file:
            file.write("0")

# Function to handle each process
def process_task(main_output):
    # Run these functions in parallel
    threads = []
    t1 = threading.Thread(target=openapp, args=(main_output,))
    t2 = threading.Thread(target=openweb, args=(main_output,))
    t3 = threading.Thread(target=generateimage, args=(main_output,))
    t4 = threading.Thread(target=play_music, args=(main_output,))
    t5 = threading.Thread(target=play_video, args=(main_output,))
    t6 = threading.Thread(target=perform_scroll_action, args=(main_output,))
    t7 = threading.Thread(target=perform_browser_action, args=(main_output,))
    t8 = threading.Thread(target=generateppt, args=(main_output,))
    t9 = threading.Thread(target=perform_media_action, args=(main_output,))
    t10 = threading.Thread(target=write, args=(main_output,))
    t11 = threading.Thread(target=press, args=(main_output,))
    t12 = threading.Thread(target=create_file, args=(main_output,))
    t13 = threading.Thread(target=find_my_ip, args=(main_output,))
    t14 = threading.Thread(target=set_brightness_windows, args=(main_output,))
    t15 = threading.Thread(target=set_volume_windows, args=(main_output,))
    t16 = threading.Thread(target=set_timer, args=(main_output,))
    # Start all threads
    for thread in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]:
        thread.start()
        threads.append(thread)

    # Wait for all to finish
    for thread in threads:
        thread.join()

while True:
    with open("state.txt", "r") as myfile:
        state = myfile.read()

    with open("input.txt", "r") as myfile:
        func = myfile.read()

    if state == "1":
        with open("input.txt", "r") as myfile:
            Main_output = myfile.read()

        shutdown(Main_output)

        if Main_output != Checker:
            if Main_output != "":
                # Process the tasks in parallel

                process_task(Main_output)

                # Add the conversation
                conversation_history.append({
                    "role": "user",
                    "content": Main_output,
                })

                # Send the conversation history to the Groq API
                chat_completion = client.chat.completions.create(
                    messages=conversation_history,
                    model="llama3-8b-8192",
                    temperature=0.5,
                    max_tokens=100,
                    top_p=1,
                    stop=None,#
                    stream=False,
                )

                # Get the AI's response
                response = chat_completion.choices[0].message.content

                # Add the AI's response to the conversation history
                conversation_history.append({
                    "role": "assistant",
                    "content": response,
                })

                with open("output.txt", "w") as file:
                    file.write(response)

                print(response)
                speak(response) 
                
            Checker = Main_output
    elif state == "0":
        if func != "":
            speak("Jarvis is not active.")
            with open("input.txt", "w") as file:
                file.write("")
#20 func