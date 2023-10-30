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
ws.geometry("400x210")
ws.eval('tk::PlaceWindow . center')
ws.resizable(False, False)

def step():
    for i in range(10):
        ws.update_idletasks()
        progress['value'] += 10
        
        time.sleep(0.1)

def clear_entry():
    yturl.delete(0, 'end')
    filepath.delete(0,'end')
    progress.step(0)


def dataSet():
    global data1, data2
    data1 = yturl.get()
    data2 = filepath.get()

resolution_label = Label(ws, text="Çözünürlük Seç:")
resolution_label.pack()

# Çözünürlük seçenekleri
resolutions = ["720p", "480p", "360p"]

resolution_var = StringVar()
resolution_var.set(" ")

resolution_menu = OptionMenu(ws, resolution_var, *resolutions)
resolution_menu.pack()

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
    selected_resolution = resolution_var.get()
    
    if selected_resolution == " ":
        messagebox.showerror(message="please choose resolution")
        return
    
    while not HasItBeenDownloaded:
        try:
            print("Başlatılıyor...")
            yt = YouTube(data1)
            print("Video Bulundu")
             # Çözünürlüğe göre uygun akışı al
            if selected_resolution == "720p":
                ys = yt.streams.get_by_resolution("720p")
            elif selected_resolution == "480p":
                ys = yt.streams.get_by_resolution("480p")
            elif selected_resolution == "360p":
                ys = yt.streams.get_by_resolution("360p")
            
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


        




    
    




