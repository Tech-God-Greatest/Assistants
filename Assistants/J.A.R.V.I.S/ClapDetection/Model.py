import torch
import librosa
import numpy as np
import sounddevice as sd
from torch import nn

# Hyperparameters and settings
sr = 22050  # Sample rate
n_mels = 40  # Number of Mel bands
max_len = 128  # Max length for padding
model_path = 'D:\Assistants\J.A.R.V.I.S\ClapDetection\clap_detection_model.pth'  # Path to the saved model

# Load the trained model
class ClapNet(nn.Module):
    def __init__(self):
        super(ClapNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32 * 10 * 32, 64)
        self.fc2 = nn.Linear(64, 2)  # Output for 2 classes (clap or noise)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.pool(x)
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load the model and set to evaluation mode
model = ClapNet()
model.load_state_dict(torch.load(model_path))
model.eval()

# Function to extract Mel-spectrogram
def extract_mel_spectrogram(audio):
    mel_spec = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mels)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    
    # Padding or truncating to max_len
    if mel_spec_db.shape[1] > max_len:
        mel_spec_db = mel_spec_db[:, :max_len]
    else:
        mel_spec_db = np.pad(mel_spec_db, ((0, 0), (0, max_len - mel_spec_db.shape[1])), mode='constant')
    
    return mel_spec_db

# Function to capture live audio and detect clap
def detect_clap():
    duration = 1  # Duration of the audio capture in seconds

    print("Listening for claps...")

    while True:
        # Capture live audio from the microphone
        audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='float32')
        sd.wait()  # Wait for the recording to complete

        # Reshape audio to match expected input format for librosa
        audio = audio.flatten()

        # Extract Mel-spectrogram
        mel_spec = extract_mel_spectrogram(audio)

        # Convert to PyTorch tensor and add necessary dimensions
        mel_spec = torch.tensor(mel_spec).unsqueeze(0).unsqueeze(0).float()  # Shape: [1, 1, n_mels, max_len]
# Set a threshold for detection
        threshold = 0.5  # Example threshold (adjust as needed)

        # Make prediction
        with torch.no_grad():
            outputs = model(mel_spec)
            probabilities = nn.functional.softmax(outputs, dim=1)
            predicted = probabilities[0][1]  # Probability of 'clap'

            if predicted.item() > threshold:  # Compare with threshold
                print("Clap detected!")
                with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "w") as file:
                    file.write("1")


# Run the live clap detection
if __name__ == '__main__':
    detect_clap()
