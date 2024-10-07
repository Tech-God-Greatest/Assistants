from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def Activate():
    print("Clap Detection Active!")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Allow microphone for your website by setting Chrome preferences
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,  # 1 means allow
    "profile.default_content_setting_values.media_stream_camera": 1,  # if you need camera as well
    "profile.default_content_setting_values.notifications": 1,
    "media_stream_mic": {"E:\\Assistants\\J.A.R.V.I.S\\Clap_Detection\\clap_detection.html": 1}  # Ensure permissions for your site
}
options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Open the target website
driver.get("E:\\Assistants\\J.A.R.V.I.S\\Clap_Detection\\clap_detection.html")

time.sleep(3)

# Locate and click the "Start Listening" button
button = driver.find_element(By.XPATH, "//button[text()='Start Clap Detection']")
button.click()

while True:
    try:
        element = driver.find_element(By.ID, "status")
        current_output = element.text
        if current_output == "Clap detected!":
            with open("E:\Assistants\J.A.R.V.I.S\input.txt","w") as file:
                file.write("Activate!")
            
    except Exception as e:
        print(f"An error occurred: {e}")