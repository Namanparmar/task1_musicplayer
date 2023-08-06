from tkinter import *
import tkinter as tk 
from PIL import ImageTk ,Image
import os
from pygame import mixer

co1 = "#ffffff"
co2 = '#333333'
co3 = '#3c1dc6'
co4 = '#cfc7f8'

window =tk.Tk()
window.title("music player")
window.geometry('510x315')
window.configure(background=co1)
window.resizable(width=False,height=False)

rootpath ='F:\\c drive\\Desktop\\music player\\music'
pattern = "*.mp3"

def play_music():
	running=listbox.get(ACTIVE)
	running_song['text'] = running
	mixer.music.load(running)
	mixer.music.play()

def pause_music():
	mixer.music.pause()	

from pygame import mixer
import os


music_directory = "F:\\c drive\\Desktop\\music player\\music"






def next_music():
	next_song = listbox.curselection()
	next_song = next_song[-1] + 1
	next_song_name =listbox.get(next_song)
	# Label.config(text)
	mixer.music.load(rootpath + "\\" + next_song_name)
	mixer.music.play()

	listbox.delete(0,END)

	show()

	listbox.select_set(next_song)
	running_song['text'] = next_song_name

def prev_music():
	next_song = listbox.curselection()
	next_song = next_song[0] - 1
	next_song_name =listbox.get(next_song)
	# Label.config(text = next_song_name)
	mixer.music.load(rootpath + "\\" + next_song_name)
	mixer.music.play()

	listbox.delete(0,END)

	show()

	listbox.select_set(next_song)
	running_song['text'] = next_song_name




left_frame = Frame( window , width=200,height= 210 , bg=co1)
left_frame.grid(row=0, column=0 ,padx= 1 , pady= 1)

right_frame = Frame( window , width=400 ,height= 220, bg=co2)
right_frame.grid(row=0, column=1 ,padx= 0)

down_frame = Frame( window , width=600 ,height= 150 , bg=co3)
down_frame.grid(row=1, column=0 ,columnspan=3,padx= 0,pady=1)

listbox = Listbox(right_frame,selectmode=SINGLE,font=("Arial 9 bold"),width=50 ,height=15,bg=co2 ,fg=co1)
listbox.grid(row=0,column=0)



w = Scrollbar(right_frame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)

img_1 = Image.open('icons/2.png')
img_1 = img_1.resize((140,140))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame,width=220,height=220, image =img_1,padx =10 )
app_image.place(x=8,y=22)

img_2 = Image.open('icons/1.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
prev_button = Button(down_frame,height=40, image =img_2,padx =10 ,command=prev_music)
prev_button.place(x=135+25,y=15+5)

img_3 = Image.open('icons/3.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(down_frame,height=40, image =img_3,padx =10 , font=("Ivy 10"),command=play_music)
play_button.place(x=180+25,y=15+5)

img_4 = Image.open('icons/4.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
pause_button = Button(down_frame,height=40, image =img_4,padx =10,command=pause_music )
pause_button.place(x=225+25,y=15+5)

img_5 = Image.open('icons/5.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
next_button = Button(down_frame,height=40, image =img_5,padx =10,command= next_music)
next_button.place(x=270+25,y=15+5)


running_song = Label(down_frame , text = "choose a song",font= ("Ivy 10"),width = 50, height =1 , padx=20, bg=co3)
running_song.place(x=25,y=0)




os.chdir(r'F:\\c drive\\Desktop\\music player\\music')
songs= os.listdir()
def show():
	for i in songs:
		listbox.insert(END,i)

show()
mixer.init()
music_state = StringVar()
music_state.set("choose one!")
window.mainloop()