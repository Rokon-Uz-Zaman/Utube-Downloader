

#author: rokon-uz-zaman roman
#Roman Youtube Downloader

import tkinter as tk
import cv2
from tkinter import filedialog
from pytube import YouTube


root=tk.Tk()
root.geometry("400x300") #window size

label1=tk.Label(root,text='Enter youtube link to download video',width=40)
label1.grid(row=1,column=1)

entry1=tk.Entry(root,width=20)
entry1.grid(row=2,column=1)

button1=tk.Button(root,text='Download',width=30,command=lambda:download())
button1.grid(row=3,column=1)

def download():
    #link = input("Enter in a link: ")
    link=entry1.get()
    print(link)

    video = YouTube(link)

    print(video.title)

    print(video.streams.filter(progressive=True))

    stream = video.streams.get_by_itag(22)
    stream.download()
    print("Video downloaded")

root.mainloop()    
    

    
    













