from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("930x620+290+40")
root.configure(bg="#0f1a2b")
root.resizable(False, False)



def open_folder():
    path = filedialog.askdirectory()
    
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)
                
def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text="Song Name: " + music_name[0:-4])



mixer.init()

Label(root, text="MUSIC PLAYER", font=("arial", 20 ,"bold")).place(x=330, y=20)

play_button = PhotoImage(file="play.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0, command=play_song, cursor="hand2").place(x=300, y=200)

resume_button = PhotoImage(file="resume.png")
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=mixer.music.unpause, cursor="hand2").place(x=400, y=200)

pause_button = PhotoImage(file="pause.png")
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=mixer.music.pause, cursor="hand2").place(x=500, y=200)


music = Label(root, text="", font="arial 15", fg="white", bg="#0f1a2b")
music.place(x=430, y=130, anchor="center")


music_frame = Frame(root, bd=2)
music_frame.place(x=20, y=350, width=890, height=250)

Button(
    root,
    text="Open Folder",
    width=110,
    height=2,
    font=("arial", 10, "bold"),
    fg="white",
    bg="#21b3de",
    command=open_folder,
    cursor="hand2"
).place(x=20, y=300)


scroll = Scrollbar(music_frame)
playlist = Listbox(
    music_frame,
    width=130,
    font="arial 10",
    bg="#333333",
    fg="gray",
    selectbackground="lightblue",
    cursor="hand2",
    bd=0,
    yscrollcommand=scroll.set,
)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()
