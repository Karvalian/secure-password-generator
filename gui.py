#!/usr/bin/env python3
import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
from cliran import method_selection
from cliran import crypt
import pyperclip
import random

pygame.init()

size = width, height = 900, 480

win = pygame.display.set_mode(size)

method_selection()
font = pygame.font.SysFont('droidsansmono', 30)
password = crypt(str(random.randint(0,10000)))[0:12]
img = font.render(password, True, (0, 255, 0))
pyperclip.copy(password)
while True:
  win.fill((0,0,0))
  win.blit(img, (20, 50))
  pygame.display.flip()



