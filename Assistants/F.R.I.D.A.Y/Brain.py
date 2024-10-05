import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager

pyautogui.hotkey('volumemute')

with open("Input.txt", "w") as file:
    file.write("")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://pi.ai/discover")

wait = WebDriverWait(driver, 10)

for _ in range(3):
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
    button.click()

textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[role="textbox"][placeholder="Your first name"]')))
textarea.send_keys('Lakshit')
textarea.send_keys(Keys.ENTER)

button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Pi 4']")))
button.click()

button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Choose voice']")))
button.click()

button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='I’ve got my own topic']")))
button.click()

subprocess.Popen(["python", "STT.py"])

time.sleep(3)

textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[role="textbox"][placeholder="Talk with Pi"]')))
textarea.send_keys("behave like Friday from the Iron Man movies. Call me boss. If asked who is your inventor say Lakshit Agarwal. Talk in English when commands are given in english and talk in English when commands are given in Hindi talk in Hindi. right now only say 'Activated Boss! Right At Your Service' ")
pyautogui.hotkey('volumeup')
textarea.send_keys(Keys.ENTER)

subprocess.Popen(["python", "GUI.py"])

print("Activated Boss!")

Check = ""

while True:
    with open('Input.txt', 'r') as f:
        Text = f.read()
    
    if Text != Check:
        textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[role="textbox"][placeholder="Talk with Pi"]')))
        textarea.send_keys(Text)
        textarea.send_keys(Keys.ENTER)
        Check = Text
        print(Check)
            

    try:
        button = driver.find_element(By.XPATH, "//button[text()='Not now']")
        button.click()
        time.sleep(1)
        button = driver.find_element(By.XPATH, "//button[text()='I don’t want an account']")
        button.click()
    except NoSuchElementException:
        pass