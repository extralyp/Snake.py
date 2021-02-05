import pygame
import random

class Food:
    def __init__(self):
        self.food_position=[]

    def get_food_position(self,gui):
        """Рандомное появление еды"""
                                  #рандомные значения из спика gui
        self.food_position=random.choice(gui.field)

    def draw_food(self,window):
        """Отрисовка еды"""
        pygame.draw.rect(window,pygame.Color("Red"),pygame.Rect(self.food_position[0],self.food_position[1],10,10))
