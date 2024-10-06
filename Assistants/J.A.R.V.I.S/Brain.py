print("You started Me")

import threading
import subprocess
import pyttsx3
from groq import Groq
from time import sleep
from Automation.Web_Open import openweb
from Automation.App_Open import openapp
from Image_Generation.image_generator import generateimage
from Youtube.Open_Youtube import play_music
from Youtube.Open_Youtube import play_video

print("imported modules")

with open("Input.txt", "w") as file:
    file.write("")

subprocess.Popen(["python", "E:\\Assistants\\A.I\\STT.py"])

sleep(15)

print("step 1 completed")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

client = Groq(api_key="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")
Checker = ""

print("step 2 completed")

conversation_history = [
    {
        "role": "system",
        "content": "You are J.A.R.V.I.S but your creator is Lakshit Agarwal. Give small responses only, like Jarvis. Lakshit Agarwal or the user is Iron Man."
    }
]

print("started!")

# Function to handle each process
def process_task(main_output):
    # Run these functions in parallel
    threads = []
    t1 = threading.Thread(target=openapp, args=(main_output,))
    t2 = threading.Thread(target=openweb, args=(main_output,))
    t3 = threading.Thread(target=generateimage, args=(main_output,))
    t4 = threading.Thread(target=play_music, args=(main_output,))
    t5 = threading.Thread(target=play_video, args=(main_output,))

    # Start all threads
    for thread in [t1, t2, t3, t4, t5]:
        thread.start()
        threads.append(thread)

    # Wait for all to finish
    for thread in threads:
        thread.join()

while True:
    with open("Input.txt", "r") as myfile:
        Main_output = myfile.read()

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
                stop=None,
                stream=False,
            )

            # Get the AI's response
            response = chat_completion.choices[0].message.content

            # Add the AI's response to the conversation history
            conversation_history.append({
                "role": "assistant",
                "content": response,
            })

            print(response)
            speak(response)

        Checker = Main_output
