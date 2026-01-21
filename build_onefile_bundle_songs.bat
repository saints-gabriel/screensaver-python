@echo off
REM Build a single-file EXE and bundle the 'songs' folder inside the EXE.
REM Warning: bundled songs are read-only in the EXE; users cannot add/remove songs.

python -m pip install --upgrade pip setuptools wheel pyinstaller
python -m PyInstaller --noconfirm --onefile --windowed --add-data "songs;songs" gui.py
python -m pip install simpleaudio


echo.
echo Build finished. The EXE is in the 'dist' folder. The bundled songs are embedded in the EXE.
pause