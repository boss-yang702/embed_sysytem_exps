import tkinter as tk
from MusicPlay import MusicPlayer
from MusicList import MusicList
import os
from tkinter import filedialog
from shutil import copyfile

class MusicButtonControl:
    def __init__(self, master, music_folder):
        #初始化 设置标题等
        self.master = master
        self.master.title("MP3 Music Player")

        self.music_list = MusicList(music_folder)
        self.music_player = MusicPlayer()

        self.label = tk.Label(master, text="播放中: ")
        self.label.pack()
        
        self.list_box=tk.Listbox(master,width=30,height=30, bg="#FFFACD")
        for item in self.music_list.music_files:
            self.list_box.insert(tk.END,item)
        self.list_box.bind("<Double-Button-1>", self.playMusic)

        self.list_box.pack(side=tk.LEFT,fill=tk.X)

        self.play_button = tk.Button(master, text="播放", command=self.play_music)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(master, text="暂停", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="停止", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(master, text="下一首", command=self.next_music)
        self.next_button.pack(side=tk.LEFT)

        self.prev_button = tk.Button(master, text="上一首", command=self.prev_music)
        self.prev_button.pack(side=tk.LEFT)

        self.add_music =tk.Button(master,text="添加音乐",command=self.add_music_func)
        self.add_music.pack(side=tk.LEFT)

    def play_music(self):
        if self.music_player.playing:
            self.music_player.unpause_music()
        else:   
            file_path = self.music_list.get_current_music()
            self.music_player.load_music(file_path)
            self.music_player.play_music()
            self.label["text"] = f"播放中: {os.path.basename(file_path)}"

    def pause_music(self):
        self.music_player.pause_music()

    def stop_music(self):
        self.music_player.stop_music()

    def next_music(self):
        self.music_player.stop_music()
        file_path = self.music_list.next_music()
        self.music_player.load_music(file_path)
        self.music_player.play_music()
        self.label["text"] = f"播放中: {os.path.basename(file_path)}"
        cur=self.list_box.curselection()
        if cur:
            selected_index=cur[0]
            next_index=(selected_index+1)%self.list_box.size()
            self.list_box.selection_clear(selected_index)
            self.list_box.selection_set(next_index)
            self.list_box.activate(next_index)

    def prev_music(self):
        self.music_player.stop_music()
        file_path = self.music_list.prev_music()
        self.music_player.load_music(file_path)
        self.music_player.play_music()
        self.label["text"] = f"播放中: {os.path.basename(file_path)}"
        cur = self.list_box.curselection()
        if cur:
            selected_index = cur[0]
            previous_index = (selected_index - 1) % self.list_box.size()
            self.list_box.selection_clear(selected_index)
            self.list_box.selection_set( previous_index)
            self.list_box.activate( previous_index)

    def playMusic(self,event):
        self.music_player.stop_music()
        index=self.list_box.curselection()
        file_path = self.music_list.get_music(index[0])
        self.music_player.load_music(file_path)
        self.music_player.play_music()
        print(file_path)
        self.label["text"] = f"播放中: {os.path.basename(file_path)}"

    def add_music_func(self):
        file = filedialog.askopenfilename()
        self.list_box.insert(tk.END,os.path.basename(file))
        copyfile(file,'music/'+os.path.basename(file)) 
        self.music_list.music_files.append(os.path.basename(file))
        pass