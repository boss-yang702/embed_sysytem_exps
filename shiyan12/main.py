import tkinter as tk
from MusicButtonControl import MusicButtonControl
#创建tk界面
root = tk.Tk()
root.geometry("700x500+200+100")
music_player = MusicButtonControl(root, "music")  # Assuming your music folder is named 'music'
root.mainloop()