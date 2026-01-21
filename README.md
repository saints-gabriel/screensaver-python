# Packaging `gui.py` to an EXE (Windows)

This project contains two convenient build scripts and short instructions to create a Windows EXE using PyInstaller.

One mode is provided:
- Bundle `songs/` into the EXE (put the .wav files inside the songs folder before compiling).

Prerequisites
- Python 3.8+ installed and on PATH
- `pip` available

Quick steps (bundle songs into EXE)
1. Put the `songs` folder you want to bundle in the project root.
2. Run:
```powershell
.\build_onefile_bundle_songs.bat
```
3. After the build completes, the EXE at `dist\gui.exe` contains the songs. Note the bundled songs are not writable or editable by users.

Notes & details
- The project contains `utils.get_songs_dir()` which:
  - prefers an external `songs/` folder next to the executable (so users can add/remove songs),
  - falls back to the PyInstaller-extracted `songs` inside `_MEIPASS`,
  - and finally uses the repo `songs/` while developing.
- On Windows `--add-data "songs;songs"` uses a semicolon between src and dest.
- `--windowed` prevents a console window from opening. Remove it to keep a console for debugging.

Troubleshooting
- If `pyinstaller` isn't installed, the build scripts will install it automatically. If you prefer to manage dependencies yourself, run:
```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install pyinstaller
```
- If the EXE fails to find songs, confirm whether you used the external `songs/` next to the EXE or bundled them with `--add-data`.
- If `simpleaudio` fails to install or play on the target machine, install the appropriate wheel for the target Python and platform. See the `simpleaudio` docs for platform-specific notes.
