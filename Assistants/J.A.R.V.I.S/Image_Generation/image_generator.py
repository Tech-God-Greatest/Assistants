import requests
from PIL import Image
from io import BytesIO

def generateimage(text):
    text = text.lower()  # Convert text to lowercase to handle case-insensitive matching
    keywords = ["generate image", "make image", "imagine image", "create an image", "create a image"]
    
    # Check if any of the keywords are present in the text
    if any(keyword in text for keyword in keywords):
        url = 'https://api.airforce/v1/imagine2'
        params = {'prompt': text}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save('generated_image.png')
            print('Image saved as generated_image.png')
        else:
            print(f'Failed to retrieve image. Status code: {response.status_code}')