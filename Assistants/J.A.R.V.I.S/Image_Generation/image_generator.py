import requests
from PIL import Image
from io import BytesIO

def generateimage(text):
    text = text.lower()  
    keywords = ["generate image", "make image", "imagine image", "create an image", "create a image"]
    
    if any(keyword in text for keyword in keywords):
        url = 'https://api.airforce/v1/imagine2'
        params = {'prompt': text}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            if response.headers['Content-Type'].startswith('image/'):
                image = Image.open(BytesIO(response.content))
                image.save('generated_image.png')
                image.show()
            else:
                print(f"Expected an image but got {response.content.decode('utf-8')}")
        else:
            print(f'Failed to retrieve image. Status code: {response.status_code}')