import time
import threading
from playsound import playsound

# Path to the alarm sound file
ALARM_SOUND_PATH = r"D:\Assistants\J.A.R.V.I.S\Time_Operations\mixkit-morning-clock-alarm-1003.wav"

def set_timer(Text):
    # Extract the relevant portion of the text
    if "set a timer for" in Text:
        # Trim irrelevant parts before the timer command
        Text = Text[Text.index("set a timer for"):]

        Time = 0
        if "hours" in Text:
            # Extract hours from the text
            Time = Text.replace("set a timer for", "").replace("hours", "").strip()
            try:
                Time = int(Time)
                seconds = Time * 3600  # Convert hours to seconds
            except ValueError:
                print("Please specify a valid number of hours.")
                return

        elif "minutes" in Text:
            # Extract minutes from the text
            Time = Text.replace("set a timer for", "").replace("minutes", "").strip()
            try:
                Time = int(Time)
                seconds = Time * 60  # Convert minutes to seconds
            except ValueError:
                print("Please specify a valid number of minutes.")
                return

        elif "seconds" in Text:
            # Extract seconds from the text
            Time = Text.replace("set a timer for", "").replace("seconds", "").strip()
            try:
                seconds = int(Time)
            except ValueError:
                print("Please specify a valid number of seconds.")
                return
        else:
            print("Please specify the time in hours, minutes, or seconds.")
            return

        # Countdown timer
        while seconds:
            hours, remainder = divmod(seconds, 3600)
            mins, secs = divmod(remainder, 60)
            timer = f'{hours:02d}:{mins:02d}:{secs:02d}'
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1

        print("\nTime's up!")
        play_alarm()


def play_alarm():
    """Play alarm sound in a loop until the user types 'stop'."""
    def sound_loop():
        """Play the alarm sound indefinitely."""
        while not stop_event.is_set():
            playsound(ALARM_SOUND_PATH)
    
    def listen_for_stop():
        """Wait for user input to stop the alarm."""
        while True:
            user_input = input("\nType 'stop' to end the alarm: ").strip().lower()
            if user_input == 'stop':
                stop_event.set()
                break

    # Create an event to signal stopping the alarm
    stop_event = threading.Event()
    
    # Start sound loop in a separate thread
    alarm_thread = threading.Thread(target=sound_loop)
    alarm_thread.start()
    
    # Wait for the user to type "stop"
    listen_for_stop()
    
    # Wait for the alarm thread to finish
    alarm_thread.join()