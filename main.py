import customtkinter as ctk
import src.home

def main():
    root = ctk.CTk()
    root.geometry("1920x1080")
    src.home.homeScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()