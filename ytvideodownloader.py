from pytube import YouTube 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


data1 = ""
data2 = ""
HasItBeenDownloaded = False

ws = Tk()
ws.title('Youtube Video Downloader')
ws.geometry("400x150")
ws.eval('tk::PlaceWindow . center')
ws.resizable(False, False)

def clear():
    yturl.text


def dataSet():
    global data1, data2
    data1 = yturl.get()
    data2 = filepath.get()


text=Label(ws,text="enter youtube url")
text.pack()

yturl=Entry(ws,width=50)
yturl.pack()

text1=Label(ws,text="enter the file path")
text1.pack()

filepath=Entry(ws,width=50)
filepath.pack()


def ytdownloader():
    global HasItBeenDownloaded, data1,data2
    data1 = yturl.get()
    data2 = filepath.get()
    
    while not HasItBeenDownloaded:
        try:
            print("Başlatılıyor...")
            yt = YouTube(data1)
            print("Video Bulundu")
            #Download video in highest resolution
            ys = yt.streams.get_highest_resolution()
            #Download video
            ys.download(data2)
            messagebox.showinfo(" ",message="Video indirildi")
            return
        except Exception as e:
            messagebox.showerror(" ",message="file path or youtube link is incorrect.")
            return 
        
button1=Button(ws,text="Download",command=ytdownloader)
button1.pack()

ws.mainloop()


        




    
    




