import pywhatkit as pw

def play_music(mcommand):
    # Keywords related to playing music
    keywords = ["play song", "start song", "turn on song", "play a song", "start the song", "play the song"]

    # Split the command into parts by 'and' to isolate different instructions
    commands = mcommand.lower().split("and")

    # Loop through each part to find the command related to playing music
    for part in commands:
        for keyword in keywords:
            if keyword in part:
                # Extract the song name: take two words right after the keyword
                song_name = part.split(keyword)[-1].strip()  # Get the part after the keyword
                song_name_words = song_name.split()[:2]  # Take only the next two words

                # Join the two words to form the song name
                song_name = " ".join(song_name_words)

                if song_name:  # Ensure song_name is not empty
                    print(f"Playing song: {song_name}")  # For debugging purposes
                    pw.playonyt(song_name)
                    return  # Exit the function once the song is found and playe
                
def play_video(vcommand):
    
    keywords = ["play video","play a video","start video","start a video","play"]

    commands = vcommand.lower().split("and")

    for part in commands:
        # Check if the word "play" or related keywords are in the part
        if any(keyword in part for keyword in keywords):
            # Extract the song name by removing the keyword and isolating the song name
            song_name = part
            for keyword in keywords:
                song_name = song_name.replace(keyword, "")

            if song_name:  # Ensure song_name is not empty
                print(f"Playing video: {song_name}")  # For debugging purposes
                pw.playonyt(song_name)
                break