# import code for encoding urls and generating md5 hashes
import urllib
import hashlib
import pygame
from random import randint

pygame.init()
# Set your variables here
size = input("Tile size ::>")
email = raw_input("String ::>")

color1 = randint(100,255)
color2 = randint(100,255)
color3 = randint(100,255)
screen = pygame.display.set_mode((size * 5, size * 5))

default = "http://www.example.com/default.jpg"

pixel =[[0]*5]*5
# construct the url
hashName = hashlib.md5(email.lower()).hexdigest()

color = hashName[0:6]
screen.fill((255,255,255))
for i in range(5):
    for j in range (5):
        hash = int(hashlib.md5(hashName[(i * 5) + j * 6:(i * 5) + j * 6 +1]).hexdigest(), 16) % 2
        if (hash == 0):
            pixel[i][j] = 0
        else:
            pixel[i][j] = 1
            pygame.draw.rect(screen, (color1,color2,color3), (i * size, j * size, size,size), 0)
            
    print " "

pygame.display.flip()
pygame.image.save(screen, "screenshot.jpg")
pygame.quit()
quit()
