import requests

def find_my_ip(Text):
    if "find my ip" in Text or "find ip" in Text or "what is my ip" in Text:
        ip_address = requests.get('https://api64.ipify.org?format=json').json()
        return ip_address["ip"]