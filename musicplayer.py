import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.iconbitmap("C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\player.ico")
root.title("Music Player")
root.config(bg='blue')
root.geometry('500x500')
root.resizable(False,False)
mixer.init()

def open():
    filepath = filedialog.askdirectory()
    os.chdir(filepath)
    songs = os.listdir(filepath)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)


def playmusic():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


def pausemusic():
    mixer.music.pause()

def playprevious():
    current_song = playlist.curselection()
    previous_song = current_song[0]-1
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    playlist.selection_clear(0,END)
    playlist.activate(previous_song)
    playlist.selection_set(previous_song)

def playnext():
    current_song = playlist.curselection()
    next_song = current_song[0]+1
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    playlist.selection_clear(0,END)
    playlist.activate(next_song)
    playlist.selection_set(next_song)
    


myimage = ImageTk.PhotoImage(file='C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\picture.png')
Label(root,image=myimage).pack()

myframe = Frame(root)
myframe.pack(padx=5,pady=5)

button = Button(myframe, text='open folder', command=open, bg='green')
button.pack()

scroll = Scrollbar(myframe)
scroll.pack(side=RIGHT, fill=Y)

playlist = Listbox(myframe, width=60, height=20, bg='black', fg='white', yscrollcommand=scroll.set)
playlist.pack()

scroll.config(command=playlist.yview)


previous = ImageTk.PhotoImage(Image.open('C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\playpreviousbutton1.png'))
previous_button = Button(root, image=previous, command=playprevious)
previous_button.place(x=180, y=460)

play = ImageTk.PhotoImage(Image.open('C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\playbutton1.png'))
play_button = Button(root, image=play, command=playmusic)
play_button.place(x=210, y=460)


pause = ImageTk.PhotoImage(Image.open('C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\pausebutton1.png'))
pause_button = Button(root, image=pause, command=pausemusic)
pause_button.place(x=240,y=460)

next = ImageTk.PhotoImage(Image.open('C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\playnextbutton1.png'))
next_button = Button(root, image=next, command=playnext)
next_button.place(x=270,y=460)


root.mainloop()



