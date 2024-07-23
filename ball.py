from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.setpos(0, 0)

    def refresh_pos(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def vert_bounce(self):
        self.y_move *= -1

    def hor_bounce(self):
        self.x_move *= -1.1
        self.y_move *= 1.1

    def point(self):
        self.setpos(0, 0)
        dir = [-1, 1]
        self.x_move = dir[randint(0, 1)] * 10
        self.y_move = dir[randint(0, 1)] * 10
        self.hor_bounce()
