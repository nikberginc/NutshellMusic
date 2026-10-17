# NutshellMusic 🎵

**Completed:** August 23, 2025

NutshellMusic is a desktop MP3 player built with **Python**, **Tkinter**, and **Pygame**. It features a custom graphical interface, drag-and-drop music importing, playlist controls, shuffle playback, and adjustable volume.

I created this project to explore desktop GUI development and combine multiple Python files into a larger application.

## Features

- **Graphical interface:** Custom buttons, icons, and a music playlist built with Tkinter.
- **Drag-and-drop importing:** Add MP3 files by dragging them onto the designated area.
- **Local music library:** Imported tracks are copied into a dedicated folder in the user's Documents directory.
- **Playback controls:** Select a song, pause or resume it, and move to the next or previous track.
- **Automatic next track:** Attempts to start the next song when the current one finishes.
- **Shuffle mode:** Switch between sequential and randomized track selection.
- **Volume controls:** Increase or decrease the volume in steps of approximately 10%, with a percentage displayed in the interface.
- **Optional generic filenames:** A checkbox lets imported MP3 files be saved under names such as `song.mp3` and `song2.mp3` instead of their original filenames. **This is not encryption.**
- **Refresh button:** Reload the playlist from the saved music folder.

## Requirements

- Python 3
- A desktop environment with Tkinter support (the provided `.ico` window icon is intended for Windows)
- The following third-party Python libraries:
  - `pygame`
  - `Pillow`
  - `tkinterdnd2`

The project also uses Python standard-library modules, including `pathlib`, `random`, and `os`.

## Installation

1. Download or clone this repository.
2. Keep the three `.py` files and the PNG/ICO interface assets together in the same directory.
3. Install the required packages:

   ```bash
   python -m pip install pygame pillow tkinterdnd2
   ```

4. From the project directory, start the application:

   ```bash
   python Main_Tkinker.py
   ```

On systems where Python is launched with `python3`, use that command instead.

**Note:** The interface and music playback have not been verified on every operating system. The application uses a Windows-style `.ico` file for its window icon.

## How to Use

### 1. Import MP3 Files

Drag one or more `.mp3` files onto the drag-and-drop area on the left side of the window.

The program copies the files into:

```text
Documents/NutshellMusic/Songs/
```

The path is created inside the current user's home directory using `Path.home()`. Non-MP3 files are skipped.

You can also place MP3 files directly into this folder and click **Refresh** to update the playlist.

### 2. Play Music

Click a track name in the playlist to start playback. Use the interface buttons to:

| Control | Action |
|---|---|
| Play / Resume | Resume paused playback |
| Pause | Pause the current track |
| Next | Play the next track |
| Previous | Return to a previous track when playback history is available |
| Shuffle | Toggle randomized song selection |
| Volume − / + | Adjust the playback volume |
| Refresh | Reload the music library |

The currently selected track is highlighted in the playlist.

### 3. Optional Generic Filenames

Before importing MP3 files, you can enable the checkbox next to the drag-and-drop area.

- **Unchecked:** The imported file keeps its original filename.
- **Checked:** The imported file receives a generic name such as `song.mp3`, `song2.mp3`, etc., using the next available filename.

This feature **only changes the copied file's name**. It does not encrypt, password-protect, or otherwise secure its contents.

## How It Works

The application is organized into three Python modules:

### `Main_Tkinker.py` — User Interface

Creates the Tkinter window, loads the image assets, displays the playlist, registers the drag-and-drop area, and connects buttons to playback functions.

It also checks periodically whether playback has finished so it can request the next song.

### `Player_functions.py` — Playback Logic

Uses `pygame.mixer.music` to load and play MP3 files. It stores the current track index, maintains playback history, manages shuffle selection, and adjusts the volume.

### `Saving_mp3.py` — Music Importing

Checks that imported files have an `.mp3` extension, creates the local music folder if needed, and copies the selected files in chunks. The optional checkbox controls how imported files are named.

## Project Structure

```text
NutshellMusic/
├── Main_Tkinker.py
├── Player_functions.py
├── Saving_mp3.py
├── NutshellMusic_icon.ico
├── *.png                    # Interface graphics and design assets
├── .gitignore
└── README.md
```

The PNG files in the repository are required for the customized controls and interface design. The actual music files are stored separately in the user's Documents folder.

## Known Limitations

- **MP3 only:** Importing supports MP3 files, not other audio formats.
- **Local library:** There is no streaming service integration or online music search.
- **No true encryption:** The filename option does not protect the audio contents.
- **Possible overwrites:** Importing a different MP3 with the same original filename while the generic-name option is off can overwrite the existing copy.
- **No playlist persistence beyond the folder:** Tracks are discovered by scanning the Songs directory; there is no separate playlist database.
- **Desktop-dependent:** The graphical interface and audio playback require a compatible desktop environment and sound system.

## Development Note

This was one of my early graphical Python applications. I used it to practice Tkinter interfaces, event-driven programming, file handling, multiple-module project organization, and audio playback with Pygame.


**Author:** [Nik Berginc](https://github.com/nikberginc)
