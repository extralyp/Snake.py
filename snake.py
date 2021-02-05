import pygame


class Snake():
    def __init__(self):
        self.head = [45, 45]
        self.body=[[45,45],[34,45],[23,45]]

    def moove_snake(self, control):
        """Движение змеи"""
        if control.flag_Direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_Direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_Direction == "UP":
            self.head[1] -= 11
        elif control.flag_Direction == "DOWN":
            self.head[1] += 11

    def animation(self):
        """меняем голову, а хвост удаляем"""
        self.body.insert(0,list(self.head))#на какой э-т будем прибавлять, прибавляем голову
        self.body.pop()#удаляем последний э-т списка

    def draw(self,window):
        """Отрисовка змеи"""
        for segment in self.body:
            pygame.draw.rect(window, (173, 255, 47), pygame.Rect(segment[0], segment[1], 10, 10))

    def end_window(self):
        """отслеживание края экрана"""
        if self.head[0]==419:
            self.head[0]=23
        elif self.head[0]==12:
            self.head[0]=419
        elif self.head[1]==23:
            self.head[1]=419
        elif self.head[1]==419:
            self.head[1]=34

    def eat(self,food,gui):
        """Поедание еды"""
        if self.head==food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indicator()

    def check_barrier(self,gui):
        """проверяет не врезалась ли змея в барьер"""
        if self.head in gui.barrier:  # если врезалась
            self.body.pop()           # удаляем сигмент
            gui.indicator.pop()
        if self.head in self.body[1:]:  # если врезалась в тело(кроме 1(головы))
            self.body.pop()
            gui.indicator.pop()

