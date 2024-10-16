import wmi

def set_brightness_windows(command):
    if "set my brightness" in command:
        percentage = command.replace("set my brightness to", "").strip()  # Extract percentage
        try:
            w = wmi.WMI(namespace='wmi')
            brightness_methods = w.WmiMonitorBrightnessMethods()[0]
            brightness_methods.WmiSetBrightness(int(percentage), 0)
            print(f"Brightness set to {percentage}%")
        except Exception as e:
            print(f"Error: {e}")