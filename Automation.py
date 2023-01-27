from pytube import YouTube
from pytube.cli import on_progress
import customtkinter

#you will need to install pytube and customtkinter for this program to work


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x425")
root.title("Automation.py")

#background functions to get specified location custom to each pc


def Audio():
    link = entry.get()
    rt = r'' + locs.get() + ':'#takes the root location
    first = '\\' + 'Users'  #creates the user file name part of the future file location
    mid = '\\' + user.get()#takes the user name 
    last = '\\' + loc.get()#takes the folder name to be used
    location = rt + first + mid + last
    aud = YouTube(link)#takes link to Youtube video
    aud = aud.streams.get_audio_only()#downloads the video in audio format only
    try:
        aud.download(location)#sends download to music folder
    except:
        print("There was a problem") #pops up in terminal
    print("The music is ready for listening") #pops up in terminal

def Download():
    link = entry.get()
    rt = r'' + locs.get() + ':'#takes the root location
    first = '\\' + 'Users'  #creates the user file name part of the future file location
    mid = '\\' + user.get()#takes the user name 
    last = '\\' + loc.get()#takes the folder name to be used
    location = rt + first + mid + last
    obj = YouTube(link)#takes link to Youtube video
    obj = obj.streams.get_highest_resolution()#downloads the video in the highest resolution
    try:
        obj.download(location)
    except:
        print("An error has occured") #pops up in terminal
    print("The video is ready for watching") #pops up in terminal

#tkinter after here
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Youtube Downloader")#title at top
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Video URL", width=300)#URL input box
entry.pack(pady=12, padx=10)

locs = customtkinter.CTkEntry(master=frame, placeholder_text="Root Letter ex: C:", width=300)#Root location input box
locs.pack(pady=12, padx=10)

user = customtkinter.CTkEntry(master=frame, placeholder_text="System User", width=300)#User input box
user.pack(pady=12, padx=10)

loc = customtkinter.CTkEntry(master=frame, placeholder_text="Location within User file", width=300)#file location input box
loc.pack(pady=12, padx=10)

#this is a work in progress
#progressbar = customtkinter.CTkProgressBar(mater=frame, on_progress_callback=on_progress)#on_progress_callback=on_progress
#progressbar.grid(row=2, column=0, padx=(20, 10), pady=(10, 10))

buttonA = customtkinter.CTkButton(master=frame, text="Audio", command=Audio)#button to download audio
buttonA.pack(pady=12, padx=10)

buttonV = customtkinter.CTkButton(master=frame, text="Video", command=Download)#button to download video
buttonV.pack(pady=12, padx=10)



root.mainloop()
