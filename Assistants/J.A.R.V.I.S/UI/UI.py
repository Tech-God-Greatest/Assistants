from flask import Flask, jsonify, send_from_directory
import os
import webbrowser
import threading


app = Flask(__name__)

@app.route('/input')
def read_input_output_files():
    input_file_path = 'D:/Assistants/J.A.R.V.I.S/input.txt'
    output_file_path = 'D:/Assistants/J.A.R.V.I.S/output.txt'
    
    input_content = ""
    output_content = ""
    
    # Check and read input.txt
    if os.path.exists(input_file_path):
        with open(input_file_path, 'r') as file:
            input_content = file.read()
    else:
        input_content = "Input file not found."
    
    # Check and read output.txt
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r') as file:
            output_content = file.read()
    else:
        output_content = "Output file not found."
    
    return jsonify({"input": input_content, "output": output_content})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

def open_browser():
    webbrowser.open('http://localhost:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()  # Open browser after a 1 second delay
    app.run(debug=True)