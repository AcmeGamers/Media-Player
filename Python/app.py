# creating using VLAN Module
# # importing vlc module
# import vlc
# import time
  
# # creating vlc media player object
# media_player = vlc.MediaPlayer("1.mp4")
  
# # start playing video
# media_player.play()
  
# # wait so the video can be played for 5 seconds
# # irrespective for length of video
# time.sleep(5)



# creating a custom made one
from tkinter import *
from pygame import mixer
import os

#########################
## Basic Configuration ##
#########################
app_name = 'music player'


root = Tk()
root.title(app_name)
root.geometry('500x500')


def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()


mixer.init()
playlist = Listbox(root, bg='green')
playlist.grid(columnspan=3)
os.chdir(os.getcwd() + '\\Python\\songs')
song = os.listdir()
for s in song:
    playlist.insert(END,s)

Button(root, text= 'play', command = playsong).grid(row = 1, column = 0)
Button(root, text= 'pause', command = pausesong).grid(row = 1, column = 1)
Button(root, text= 'stop', command = stopsong).grid(row = 1, column = 2)
Button(root, text= 'resume', command = resumesong).grid(row = 1, column = 3) 
mainloop()

