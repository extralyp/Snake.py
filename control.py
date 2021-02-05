import pygame
from pygame.locals import *


class Control():
    def __init__(self):  # конструктор
        self.run = True
        self.flag_Direction = "RIGHT"  # управление с помощью флага

    def control(self):
        """У"""
        for event in pygame.event.get():
            if event.type == QUIT:  # выход из приложения
                self.run = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.flag_Direction!="LEFT":
                    self.flag_Direction = "RIGHT"
                elif event.key == K_LEFT and self.flag_Direction!="RIGHT":
                    self.flag_Direction = "LEFT"
                elif event.key == K_DOWN and self.flag_Direction!="UP":
                    self.flag_Direction = "DOWN"
                elif event.key == K_UP and self.flag_Direction!="DOWN":
                    self.flag_Direction = "UP"
                elif event.key == K_ESCAPE:
                    self.run = False

