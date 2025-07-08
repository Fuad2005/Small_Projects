import tkinter as tk
from tkinter import messagebox
import pygame

# initialize pygame mixer
pygame.mixer.init()

# load sound files
c = pygame.mixer.Sound("./sounds/c.wav")
d = pygame.mixer.Sound("./sounds/d.wav")
e = pygame.mixer.Sound("./sounds/e.wav")
f = pygame.mixer.Sound("./sounds/f.wav")
g = pygame.mixer.Sound("./sounds/g.wav")
a = pygame.mixer.Sound("./sounds/a.wav")
b = pygame.mixer.Sound("./sounds/b.wav")

# initialize tkinter
root = tk.Tk()
root.title("Piano")

# function to play sound
def play_sound(sound):
    sound.play()

# create buttons for each note
c_button = tk.Button(root, text="C", command=lambda: play_sound(c))
c_button.pack()
d_button = tk.Button(root, text="D", command=lambda: play_sound(d))
d_button.pack()
e_button = tk.Button(root, text="E", command=lambda: play_sound(e))
e_button.pack()
f_button = tk.Button(root, text="F", command=lambda: play_sound(f))
f_button.pack()
g_button = tk.Button(root, text="G", command=lambda: play_sound(g))
g_button.pack()
a_button = tk.Button(root, text="A", command=lambda: play_sound(a))
a_button.pack()
b_button = tk.Button(root, text="B", command=lambda: play_sound(b))
b_button.pack()

# run the GUI
root.mainloop()
