from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
import time
import os

def generateppt(Text):
    # Create a list of phrases to check
    phrases = [
        "generate ppt",
        "generate powerpoint",
        "make powerpoint",
        "generate a ppt",
        "generate a powerpoint",
        "make a powerpoint",
        "generate an ppt",
        "generate an powerpoint",
        "make an powerpoint",
        "make a ppt",
        "make an ppt",
        "make a presentation",
        "generate a presentation"
    ]

    # Check if any phrase is in the input text
    if any(phrase in Text.lower() for phrase in phrases):
        os.system("taskkill /F /IM msedge.exe /T")

        # Set up Edge options to use your default profile
        edge_options = Options()
        edge_options.add_argument("user-data-dir=C:\\Users\\Laksh\\AppData\\Local\\Microsoft\\Edge\\User Data")  # Path to the user data directory
        edge_options.add_argument("profile-directory=Default")  # Use 'Default' profile or 'Profile 1', 'Profile 2', etc.

        # Initialize Edge driver with the specified options
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)
        driver.get("https://gamma.app/create/generate")

        time.sleep(3)

        textarea = driver.find_element(By.CSS_SELECTOR, "textarea.chakra-textarea.css-17hrdsl")
        textarea.send_keys(Text)

        generate_button = driver.find_element(By.CSS_SELECTOR, "button.chakra-button.css-y0msvc")
        generate_button.click()

        time.sleep(3)

        button = driver.find_element(By.CSS_SELECTOR, '.chakra-button.css-446ahm')
        button.click()

        time.sleep(3)

        button = driver.find_element(By.CSS_SELECTOR, '.chakra-button.css-446ahm')
        button.click()

        time.sleep(7)

        button = driver.find_element(By.CSS_SELECTOR, '.chakra-button.css-2fawvm')
        button.click()

        while "close presentation" not in Text:
            time.sleep(1)
            print(Text)