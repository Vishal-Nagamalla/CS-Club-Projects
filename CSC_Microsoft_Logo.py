import pygame
pygame.init()

display = pygame.display.set_mode((800,600))

x = 100
y = 100
a = 350
b = 100

c = 100
d = 350
j = 350
k = 350

width = 200
hight = 200

Red = (255, 0 , 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

while True:
  pygame.display.flip()
  pygame.draw.rect(display, Red, (x, y, width, hight))
  pygame.draw.rect(display, Green, (a, b, width, hight))
  pygame.draw.rect(display, Blue, (c, d, width, hight))
  pygame.draw.rect(display, Yellow, (j, k, width, hight))