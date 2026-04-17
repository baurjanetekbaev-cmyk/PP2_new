import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((500,500))
black=(0,0,0)
screen.fill(black)
isD=True
index=0
sounds = [
    "practice9/music_player/music/bransboynd-groovy-vibe-427121.mp3",
    "practice9/music_player/music/kornevmusic-upbeat-happy-corporate-487426.mp3"
]
isPaused=False
isPlayed=True

while isD:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isD=False
            pygame.quit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            if index==len(sounds)-1:
                index=0
            else: index+=1

            isPaused=False
            isPlayed=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            if index==0:
                index=len(sounds)-1
            else:
                index-=1
            isPaused=False
            isPlayed=True

        if event.type==pygame.KEYDOWN and isPlayed:
            if isPaused:
                pygame.mixer.music.unpause()
                isPaused=not isPaused
            else:
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play(0)
            isPlayed=not isPlayed
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE and not isPlayed:
            pygame.mixer.music.pause()
            isPlayed=not isPlayed
            isPaused=not isPaused
    pygame.display.flip()