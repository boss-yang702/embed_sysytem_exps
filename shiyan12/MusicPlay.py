from pygame import mixer

class MusicPlayer:
    def __init__(self):
        mixer.init()
        self.playing = False

    def load_music(self, file_path):
        mixer.music.load(file_path)

    def play_music(self):
        if not self.playing:
            mixer.music.play()
            self.playing = True

    def pause_music(self):
        mixer.music.pause()

    def unpause_music(self):
        mixer.music.unpause()

    def stop_music(self):
        mixer.music.stop()
        self.playing = False
