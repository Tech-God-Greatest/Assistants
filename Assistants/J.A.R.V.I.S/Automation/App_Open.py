import pyautogui
from Automation.App_Data import app_commands
import time

def openapp(app_name_input):
    app_name_input = app_name_input.strip().lower()

    matching_apps = [name for name in app_commands if name.lower() in app_name_input]

    if matching_apps:
        try:
            app_name = matching_apps[0]

            # Open the app
            pyautogui.press("win")
            time.sleep(0.7)
            pyautogui.typewrite(app_name)
            time.sleep(0.7)
            pyautogui.press("enter")
            print(f"Opening {app_name}...")
        except Exception as e:
            print(f"Error: Unable to open {app_name}. {e}")