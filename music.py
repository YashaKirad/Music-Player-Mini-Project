from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk, filedialog
from pygame import mixer
import os


root=Tk()
root.title("Music Player")
root.geometry("920x670+20+85")
root.configure(bg="#ffffff")

mixer.init()

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


top=PhotoImage(file="images/top.png")
Label(root,image=top,bg="#FFFFFF").pack()

logo=PhotoImage(file="images/logo.png")
Label(root,image=logo,bg="#FFFFFF").place(x=65,y=110)

play=PhotoImage(file="images/play.png")
Button(root,image=play,bg="#FFFFFF",bd=0,command=play_song).place(x=100, y=400)

stop=PhotoImage(file="images/stop.png")
Button(root,image=stop,bg="#FFFFFF",bd=0,command=mixer.music.stop).place(x=30, y=500)

resume=PhotoImage(file="images/resume.png")
Button(root,image=resume,bg="#FFFFFF",bd=0,command=mixer.music.unpause).place(x=115, y=500)

pause=PhotoImage(file="images/pause.png")
Button(root,image=pause,bg="#FFFFFF",bd=0,command=mixer.music.pause).place(x=200, y=500)

menu=PhotoImage(file="images/menu.png")
Button(root,image=menu,bg="#FFFFFF").pack(padx=10, pady=50, side=RIGHT)

frame=Frame(root,bd=2,relief=RIDGE).place(x=330,y=350,width=560,height=250)
Button(root,text="Open Folder", width=15,height=2,command=open_folder,font=("arial",10,"bold"),fg="Black", bg="#21b3de").place(x=330,y=300)


scroll=Scrollbar(frame)
playlist=Listbox(frame,width=80,height=15,font=("arial",10),bg="#333333",fg="grey",bd=0,cursor="hand2",yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.place(x=330,y=350)

root.mainloop()