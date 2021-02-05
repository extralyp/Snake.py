import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake game")
control = Control()  # объект класса
snake = Snake()  # объект класса
gui = Gui()  # объект класса
food=Food()
gui.init_field()
food.get_food_position(gui)
speed = 0

while control.run:
    gui.check_win_lose()
    control.control()
    window.fill((255, 255, 255))
    if gui.game=="GAME":
        snake.draw(window)  # рисуем голову змеи
        food.draw_food(window)  # рисуем еду
    elif gui.game=="WIN":
        gui.draw_win(window)
    elif gui.game=="LOSE":
        gui.draw_lose(window)

    gui.draw_indicator(window)  # рисуем индикатор
    gui.draw_level(window)  # рисуем карту
    pygame.display.update()  # обновление, что бы появился персонаж
    if speed % 10 == 0 and gui.game=="GAME":
        snake.moove_snake(control)
        snake.check_barrier(gui)
        snake.eat(food,gui)
        snake.end_window()
        snake.animation()
    speed += 1
    pygame.display.flip()  # отображение окна
