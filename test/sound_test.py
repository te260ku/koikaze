import pygame.mixer
import time


pygame.mixer.init()

pygame.mixer.music.load("walk.mp3")
pygame.mixer.music.play(1)

time.sleep(30)
pygame.mixer.music.stop()
