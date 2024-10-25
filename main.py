import customtkinter as ctk
from tkVideoPlayer import tkvideoplayer

def home(root):
    videoplayer = tkvideoplayer.TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"./assets/space_background.gif")

    def video_ended(event):
        videoplayer.seek(1)
        videoplayer.play()

    videoplayer.bind("<<Ended>>", video_ended)

    videoplayer.pack(expand=True, fill="both")

    videoplayer.play()

def main():
    root = ctk.CTk()

    home(root)

    root.mainloop()

if __name__ == "__main__":
    main()
