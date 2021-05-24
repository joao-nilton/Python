''' import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('oceansgull.mp3')
pygame.music.play()
pygame.event.wait()''' # não funcionou.

'''
import pygame
# print (pygame.ver)
pygame.init()
pygame.mixer.music.load('needles-n-pins.mp3')
pygame.mixer.music.play()
pygame.event.wait()




from pygame import mixer, event
mixer.init()
mixer.music.load('oceansgull.mp3')
mixer.music.play()
event.wait()

'''
'''
import pygame
arquivo = 'needles-n-pins.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
pygame.event.wait()
'''
from pygame import mixer
mixer.init() 
mixer.music.load('oceansgull.mp3')
mixer.music.play()
import time
time.sleep(360)
