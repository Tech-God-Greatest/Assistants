import re
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Function to set the system volume
def set_volume_windows(command):
    if "set" in command and "volume" in "command":
        # Extract the number using regex
        percentage = re.findall(r'\d+', command)
        if percentage:  # Check if we found a number
            percentage = int(percentage[0])  # Convert it to an integer
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            # Convert percentage to scalar value (0.0 to 1.0)
            volume.SetMasterVolumeLevelScalar(percentage / 100, None)
            print(f"Volume set to {percentage}%")
        else:
            print("No valid volume percentage found in the command")