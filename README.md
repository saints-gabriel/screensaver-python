# Packaging `gui.py` to an EXE (Windows)

This project contains a convenient build scripts and short instructions to create a Windows EXE using PyInstaller.

- Bundle `songs/` into the EXE (put the .wav files inside the songs folder before compiling).
- You will need C++ > v14.0 installed into your machine due to the simpleaudio library.

Prerequisites
- Python 3.8+ installed and on PATH
- C++ 14.0 or higher
- `pip` available

Quick steps (bundle songs into EXE)
1. Put the `songs` folder you want to bundle in the project root.
2. The songs need to be in `.wav` format
3. Run:
```powershell
.\build_onefile_bundle_songs.bat
```
3. After the build completes, the EXE at `dist\gui.exe` contains the songs. Note the bundled songs are **NOT** writable or editable by users.

Troubleshooting
- If `pyinstaller` isn't installed, the build scripts will install it automatically. If you prefer to manage dependencies yourself, run:
```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install pyinstaller
python -m pip install simpleaudio
```
- If the EXE fails to find songs, confirm whether you used the external `songs/` next to the EXE or bundled them with `--add-data`.

# Simpleaudio not installing

- If `simpleaudio` fails to install or play on the target machine (probably due to the C++ issue explained earlier), install the appropriate wheel for the target Python and platform. See the `simpleaudio` docs for platform-specific notes.
