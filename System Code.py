# code created to learn more about python
# created by Gabriel Hernandes
# linkedin: https://br.linkedin.com/in/gabriel-hernandes-4a3b8b248?trk=people-guest_people_search-card
# github: https://github.com/Gabriel-Hernandess/Pytube-Video-Download
# Fork ainda em desenvolvimento

from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image
from urllib.request import urlopen
from tkinter import Button

# https://youtu.be/DKbfBSrjVHA (link teste)

def download_mp4():
    url = YouTube(str(link.get()))
    url = url.streams.get_highest_resolution()
    url.download(filename=url.title+".mp4")

def download_mp3():
    url = YouTube(str(link.get()))
    url = url.streams.filter(only_audio=True).first()
    url.download(filename=url.title+".mp3")

def download():
    
    url = YouTube(str(link.get()))
    Label(sistem_pytube, text=url.title, bg="white", fg="black", bd=3, highlightbackground="grey", highlightthickness=3).place(x=230, y=205)

    Button(sistem_pytube, text="MP4 Download", bd=5, highlightbackground = "black", highlightthickness = 3, bg="white", command=download_mp4).place(x=230, y=550)
    Button(sistem_pytube, text="MP3 Download", bd=5, highlightbackground = "black", highlightthickness = 3, bg="white",command=download_mp3).place(x=450, y=550)

    u = urlopen(url.thumbnail_url)
    raw_data = u.read()
    u.close

    image = ImageTk.PhotoImage(data=raw_data)
    Label(sistem_pytube, image = image, width=450, height=250, bd=1,  highlightbackground="black", highlightthickness=2).place(x=180, y=250).pack()


sistem_pytube=Tk()
sistem_pytube.title("PyTube Download")
sistem_pytube.geometry("800x750")
sistem_pytube.minsize(800, 750) 
sistem_pytube.maxsize(800, 750)
sistem_pytube.configure(background="white")

text_main=Label(sistem_pytube, text="Youtube Video Download", background="red", foreground="white")
text_main.place(x=280, y=20, width=220, height=30)

text_instruct=Label(sistem_pytube, text="Please, enter a video Url", bg="white" ,fg="black")
text_instruct.place(x=195, y=72)

link=Entry(sistem_pytube, background="grey")
link.place(x=170, y=100, width=280, height=30)

download_btn = Button(sistem_pytube, text="Search", bd=5, highlightbackground = "black", highlightthickness = 3, bg="white", command=download).place(x=490, y=95)

sistem_pytube.mainloop()
