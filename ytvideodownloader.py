from pytube import YouTube 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time

data1 = ""
data2 = ""
HasItBeenDownloaded = False

ws = Tk()
ws.title('Youtube Video Downloader')
ws.geometry("400x150")
ws.eval('tk::PlaceWindow . center')
ws.resizable(False, False)

def step():
    for i in range(10):
        ws.update_idletasks()
        progress['value'] += 10
        
        time.sleep(0.2)

def clear_entry():
    yturl.delete(0, 'end')
    filepath.delete(0,'end')
    progress.step(0)


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

progress = ttk.Progressbar(ws, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10) 


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
            step()
            messagebox.showinfo(" ",message="Video indirildi")
            clear_entry()
            return
        except Exception as e:
            messagebox.showerror(" ",message="file path or youtube link is incorrect.")
            return 
        
button1=Button(ws,text="Download",command=ytdownloader)
button1.pack()

ws.mainloop()


        




    
    




