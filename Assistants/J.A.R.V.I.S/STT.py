from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Setting up Chrome options to allow microphone permissions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Allow microphone for your website by setting Chrome preferences
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,  # 1 means allow
    "profile.default_content_setting_values.media_stream_camera": 1,  # if you need camera as well
    "profile.default_content_setting_values.notifications": 1,
    "media_stream_mic": {"https://allorizenproject1.netlify.app": 1}  # Ensure permissions for your site
}
options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Open the target website
driver.get("https://allorizenproject1.netlify.app/")

# Wait for the page to load
time.sleep(3)

# Locate and click the "Start Listening" button
button = driver.find_element(By.XPATH, "//button[text()='Start Listening']")
button.click()

# Monitor and log the output continuously
last_output = ""

while True:
    try:
        element = driver.find_element(By.ID, "output")
        current_output = element.text

        if current_output != last_output:
            with open("input.txt", "w") as file:
                file.write(current_output)
                print("User: " + current_output)
                last_output = current_output
            
    except Exception as e:
        print(f"An error occurred: {e}")