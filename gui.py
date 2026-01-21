import threading
import tkinter as tk
import tkinter.messagebox as messagebox
import viewer
import os
from functools import partial
from utils import get_songs_dir

SONGS_DIR = get_songs_dir()
songs = []
if os.path.isdir(SONGS_DIR):
    songs = [f for f in os.listdir(SONGS_DIR) if f.lower().endswith(".wav")]

root = tk.Tk()
root.title("Screensaver Menu")
root.geometry("800x650")

label = tk.Label(root, text="Press Start to launch the screensaver with the selected song", font=("Jetbrains Mono", 10))
label.pack(pady=12)


def checkbox_list(parent, items):
    container = tk.Frame(parent)
    canvas = tk.Canvas(container, height=250)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    inner_frame = tk.Frame(canvas)

    inner_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=inner_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    vars = []

    def select_only(index):
        for i, v in enumerate(vars):
            v.set(i == index)

    for i, item in enumerate(items):
        v = tk.BooleanVar(value=False)
        cb = tk.Checkbutton(inner_frame, text=item, variable=v, anchor="w", justify="left",
                            font=("Jetbrains Mono", 10), command=partial(select_only, i))
        cb.pack(fill="x", padx=4, pady=2)
        vars.append(v)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    return container, vars


checkbox_frame, vars = checkbox_list(root, songs)
checkbox_frame.pack(padx=20, pady=6, fill="x")


def rebuild_song_list():
    """Re-scan the songs folder and rebuild the checkbox list so new files show up."""
    global SONGS_DIR, songs, checkbox_frame, vars, notice
    # destroy existing checkbox frame
    try:
        checkbox_frame.destroy()
    except Exception:
        pass

    # re-resolve songs dir and list
    SONGS_DIR = get_songs_dir()
    songs = []
    if os.path.isdir(SONGS_DIR):
        songs = [f for f in os.listdir(SONGS_DIR) if f.lower().endswith(".wav")]

    # rebuild UI
    checkbox_frame_new, vars_new = checkbox_list(root, songs)
    checkbox_frame = checkbox_frame_new
    vars = vars_new
    checkbox_frame.pack(padx=20, pady=6, fill="x")

    # update notice label
    try:
        notice.destroy()
    except Exception:
        pass
    if not songs:
        notice = tk.Label(root, text="No .wav files found in the 'songs' folder.", fg="red", font=("Jetbrains Mono", 10))
        notice.pack(pady=6)


def get_selected_song():
    for i, v in enumerate(vars):
        if v.get():
            return songs[i]
    return None


def on_button_click():
    selected = get_selected_song()
    if not selected:
        if songs:
            selected = songs[0]
        else:
            messagebox.showwarning("No songs", "No .wav files were found in the 'songs' directory.")
            return

    button.config(state="disabled")

    song_path = os.path.join(SONGS_DIR, selected)
    threading.Thread(target=lambda: viewer.main(audio_file=song_path, fullscreen=True), daemon=True).start()


refresh_button = tk.Button(root, text="Refresh", font=("Jetbrains Mono", 10), command=rebuild_song_list)
refresh_button.pack(pady=6)

button = tk.Button(root, text="Start", font=("Jetbrains Mono", 10), command=on_button_click)
button.pack(pady=10)

if not songs:
    notice = tk.Label(root, text="No .wav files found in the 'songs' folder.", fg="red", font=("Jetbrains Mono", 10))
    notice.pack(pady=6)

root.mainloop()
