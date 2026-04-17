import pygame

class MusicPlayer:
    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist
        self.index = 0
        self.paused = False

    def play(self):
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()
        self.paused = False

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def unpause(self):
        pygame.mixer.music.unpause()
        self.paused = False

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def current_track(self):
        return self.playlist[self.index]