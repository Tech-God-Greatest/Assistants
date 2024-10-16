from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def generatevid(Text):
    # Phrases to detect for video generation
    phrases = [
        "generate vid", "generate video", "make video", "generate a vid",
        "generate a video", "make a video", "generate an vid", 
        "generate an video", "make an video", "make a vid", "make an vid"
    ]

    # Check if input text contains any of the key phrases
    if any(phrase in Text.lower() for phrase in phrases):
        # Kill any running Edge processes (use with caution)
        os.system("taskkill /F /IM msedge.exe /T")

        # Set up Edge options with the default profile
        edge_options = Options()
        edge_options.add_argument("user-data-dir=C:\\Users\\Laksh\\AppData\\Local\\Microsoft\\Edge\\User Data")  # Adjust path
        edge_options.add_argument("profile-directory=Default")
        edge_options.add_argument("--start-minimized")  # Start minimized
        time.sleep(2)
        # Initialize Edge WebDriver
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)

        time.sleep(3)
        
        # Open the VEED AI video generation tool
        driver.get("https://www.veed.io/tools/ai-video")

        time.sleep(6)

        try:
            # Wait for the text area to appear and input the Text
            textarea = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-testid='@text-to-video/form/textarea']"))
            )
            textarea.send_keys(Text)

            time.sleep(3)
            # Click the "Generate" button
            generate_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='@text-to-video/form/generate']")
            generate_button.click()

            # Wait for the social step button to be clickable, then click
            social_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='@ai-text-to-video/social-step/cta']"))
            )
            social_button.click()

            # Wait for the script step button to be clickable, then click
            script_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='@ai-text-to-video/script-step/cta']"))
            )
            script_button.click()

            # Wait for the publish button to be clickable, then click
            publish_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='@header-controls/publish-button']"))
            )
            publish_button.click()

            driver.execute_script("document.querySelector('.sc-koqmod.nets.modalOverlay').style.display = 'none';")

            accept_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='@component/terms-consent-modal/btn']"))
            )

            accept_button.click()

            time.sleep(5)

            # Wait for the export button to be clickable, then click to export the video
            export_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='@export/export-button']"))
            )
            export_button.click()

            time.sleep(25)

            driver.maximize_window()

        except Exception as e:
            print(f"An error occurred: {e}")
# Example usage
generatevid("generate a video about AI automation")