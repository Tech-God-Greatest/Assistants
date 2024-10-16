import pyautogui

def press(Text):
    if "press" in Text or "Press" in Text:
        Press = Text.replace("Press ", "")
        Press = Text.replace("press ", "")
        pyautogui.press(Press)