print("You started Me")

from groq import Groq
import subprocess
import pyttsx3
from time import sleep

print("imported modules")

with open("Input.txt", "w") as file:
    file.write("")

subprocess.Popen(["python", "E:\Assistants\A.I\STT.py"])

sleep(10)

print("step 1 completed")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

client = Groq(
    api_key="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",
)
Checker = ""

print("step 2 completed")

conversation_history = [
    {
        "role": "system",
        "content": "You are voice assistant created by Lakshit Agarwal. You have to give small responses only like A Helpful daily life AI. You are ment to help people in my daily tasks"
    }
]

print("started !")

while True:
    with open("input.txt", "r") as myfile:
        Main_output = myfile.read()

    if Main_output != Checker:
        if Main_output != "":
    # Add the user's message to the conversation history
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
        
