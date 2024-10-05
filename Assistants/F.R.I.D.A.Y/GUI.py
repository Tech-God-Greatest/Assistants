import http.server
import socketserver
import webbrowser
import os
import pyautogui
import time
PORT = 8000
DIRECTORY = os.path.abspath("E:\\Assistants\\F.R.I.D.A.Y")
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
def start_server():
    handler = MyRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        time.sleep(2)
        pyautogui.press('f11')
        print("clicked f11")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()