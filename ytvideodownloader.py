from pytube import YouTube 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import os
from urllib.parse import urlparse

data1 = ""
data2 = ""
HasItBeenDownloaded = False

ws = Tk()
ws.title('Youtube Video Downloader')
ws.geometry("400x210")
ws.eval('tk::PlaceWindow . center')
ws.resizable(False, False)

def generate_unique_filename(yt):
    #Generate a unique filename from URL or title
    video_title = ''.join(e for e in yt.title if e.isalnum())
    file_extension = yt.streams.get_highest_resolution().mime_type.split("/")[-1]
    
    return f"{video_title}.{file_extension}"

def get_available_filename(full_path):
    #If the file already exists, add a unique number to the end of the file name
    base, ext = os.path.splitext(full_path)
    i = 1
    while os.path.exists(full_path):
        full_path = f"{base}_{i}{ext}"
        i += 1
    return full_path

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def is_valid_file_path(file_path):
    try:
        return os.path.exists(file_path)
    except Exception:
        return False

#progressbar
def step(a):
    for i in range(a):
        ws.update_idletasks()
        progress['value'] += 10
        time.sleep(0.1)

def clear_entry():
    yturl.delete(0, 'end')
    filepath.delete(0,'end')
    
def clear_progress_bar():
    progress['value'] = 0


def dataSet():
    global data1, data2
    data1 = yturl.get()
    data2 = filepath.get()

resolution_label = Label(ws, text="resolution")
resolution_label.pack()

#resolution options
resolutions = ["720p", "360p"]

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
    if not data1 or not data2:
        messagebox.showerror("Error", "URL and file path fields must be filled.")
        return
    
    if not is_valid_url(data1):
        messagebox.showerror("Error", "Invalid URL. Please enter a correct YouTube URL.")
        return
    
    if not is_valid_file_path(data2):
        messagebox.showerror("Error", "Invalid file path. Please enter a valid file path.")
        return
    
    while not HasItBeenDownloaded:
        try:
            yt = YouTube(data1)
            step(3)
            unique_filename = generate_unique_filename(yt)
            full_path = os.path.join(data2, unique_filename)
            #print("video found")
            #Select appropriate stream based on resolution
            if selected_resolution == "720p":
                ys = yt.streams.get_by_resolution("720p")
            elif selected_resolution == "360p":
                ys = yt.streams.get_by_resolution("360p")
            step(2)    
                 #Check the directory of downloaded videos
            if os.path.isfile(full_path):
                #If the file exists, create a unique name
                full_path = get_available_filename(full_path)
            step(2)
            #Download video
            ys.download(data2, filename=os.path.basename(full_path))
            step(3)
            messagebox.showinfo(" ",message="Video downloaded")
            clear_entry()
            clear_progress_bar()
            return
        except Exception as e:
            messagebox.showerror(" ",message="Error, check data again or check your internet connection")            
            clear_progress_bar()
            return 
        
button1=Button(ws,text="Download",command=ytdownloader)
button1.pack()

ws.mainloop()


        




    
    




