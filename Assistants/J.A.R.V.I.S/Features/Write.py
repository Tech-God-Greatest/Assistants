import pyautogui

def write(Text):
    if "right" in Text or "type" in Text:
        Write = Text.replace("Write ", "")
        Write = Text.replace("write ", "")
        pyautogui.write(Write + " ")