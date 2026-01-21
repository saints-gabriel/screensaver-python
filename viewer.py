import os
import turtle
import random
import simpleaudio as sa
from typing import Optional
import tkinter as tk
from utils import get_songs_dir

colors = ["red", "blue", "green", "yellow", "purple", "orange"]


def main(audio_file: Optional[str] = None, fullscreen: bool = False):
 
    if audio_file is None:
        audio_file = None
        songs_dir = get_songs_dir()
        if os.path.isdir(songs_dir):
            for f in os.listdir(songs_dir):
                if f.lower().endswith(".wav"):
                    audio_file = os.path.join(songs_dir, f)
                    break

    wave_obj = None
    if audio_file:
        try:
            wave_obj = sa.WaveObject.from_wave_file(audio_file)
        except Exception as e:
            print(f"Warning: could not load '{audio_file}' - audio disabled:", e)

    screen = turtle.Screen()
    screen.bgcolor("black")
    if fullscreen:
        try:
            screen.setup(width=1.0, height=1.0)
        except Exception:
            pass
        try:
            root = screen._root
            root.attributes("-fullscreen", True)
        except Exception:
            try:
                root = screen._rootwindow
                root.attributes("-fullscreen", True)
            except Exception:
                pass

    pen = turtle.Turtle()
    pen.hideturtle()

    def draw():
        pen.pensize(2)
        pen.speed(100)
        pen.pencolor(random.choice(colors))
        pen.penup()
        pen.goto(random.randint(-700, 700), random.randint(-400, 400))
        pen.pendown()

    draw()

    play_obj = None
    if wave_obj:
        try:
            play_obj = wave_obj.play()
        except Exception as e:
            print("Warning: could not play audio:", e)

    def step():
        try:
            pen.forward(10)
            random.choice([pen.right, pen.left, pen.forward, pen.backward])(90)
            if random.random() < 0.02:
                draw()
        except turtle.Terminator:
            return
        screen.ontimer(step, 20)

    def stop_music():
        nonlocal play_obj
        if play_obj:
            try:
                play_obj.stop()
            except Exception:
                pass

    screen.listen()
    screen.onkey(stop_music, "s")

    root = tk.Tk()

    label = tk.Label(root, text="Press 's' to stop the music", font=("Jetbrains Mono", 10))
    label.pack(pady=20, padx=10)
    button = tk.Button(root, text="Ok", font=("Jetbrains Mono", 10), command=root.destroy)
    button.pack(pady=10, padx=10)


    step()
    screen.mainloop()