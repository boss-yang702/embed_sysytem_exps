import os
import tkinter as tk
class MusicList():
    def __init__(self,music_folder):

        self.music_folder = music_folder
        self.music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
        self.current_index = 0
        

    def get_current_music(self):
        return os.path.join(self.music_folder, self.music_files[self.current_index])

    def next_music(self):
        self.current_index = (self.current_index + 1) % len(self.music_files)
        return self.get_current_music()

    def prev_music(self):
        self.current_index = (self.current_index - 1) % len(self.music_files)
        return self.get_current_music()
    
    def get_music(self,index):
        self.current_index=index
        return os.path.join(self.music_folder,self.music_files[index])