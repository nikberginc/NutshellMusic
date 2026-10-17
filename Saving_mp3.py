from pathlib import Path
import time

def copy_mp3(music_to_transfer: Path, encrypt: bool, draged_song_name="song"):


    #will check if files are anything else then mp3 and if yes the program does nothinkg
    if music_to_transfer.suffix.lower() != ".mp3":
        return

    # Will create folders than store the music, if files are already created than it will do nothin
    folder_path = Path.home() / "Documents" / "NutshellMusic" / "Songs"
    folder_path.mkdir(parents=True, exist_ok=True)

    if encrypt:
        #strts from 1 and the next while true will take care of it
        mp3_count = 1
        #
        #will check if songx.mp3 already exist and if yes the loop will continue until the song x.mp3 is unique
        while True:

            
            if mp3_count == 1:
                help_for_counting = folder_path / "song.mp3"
            else:
                help_for_counting = folder_path / f"song{mp3_count}.mp3"

            if help_for_counting.exists() or help_for_counting.exists():
                mp3_count +=1
            else:
                break
        #
        #
        #Will check if num is 1 and if so it wont give it a number
        if mp3_count == 1:
            file_path = folder_path / "song.mp3"

        else:
            # File path (inside the folder)
            file_path = folder_path / f"song{mp3_count}.mp3"

    #the song will be coppyed to the folder
    else:
        file_path = folder_path / f"{draged_song_name}.mp3"



    # Copy the mp3
    with open(music_to_transfer, "rb") as src, open(file_path, "wb") as dst:
        for chunk in iter(lambda: src.read(65536), b""):
            dst.write(chunk)