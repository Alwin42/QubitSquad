import customtkinter as ctk
from tkVideoPlayer import tkvideoplayer

def homeScreen(root):
    videoplayer = tkvideoplayer.TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"./assets/space_background2.mp4")

    def video_ended(event):
        videoplayer.seek(1)
        videoplayer.play()

    videoplayer.bind("<<Ended>>", video_ended)

    videoplayer.pack(expand=True, fill="both")

    videoplayer.play()