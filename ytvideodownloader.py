from pytube import YouTube 
HasItBeenDownloaded = False
while HasItBeenDownloaded==False:
    try:
        yturl = input("enter youtube link :")
        filepath = input("enter the file path to download :")
        yt = YouTube(yturl)
        #Download video in highest resolution
        ys = yt.streams.get_highest_resolution()
        
        #Download video
        ys.download(filepath)
        print("download completed")
        HasItBeenDownloaded = True
    except:
        print("The link or file path is incorrect")
        
        


    
    






