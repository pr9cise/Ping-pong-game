from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setpos(x, y)

    def go_up(self):
        if self.ycor() < 240:
            self.setheading(90)
            self.forward(20)

    def go_down(self):
        if self.ycor() > -240:
            self.setheading(270)
            self.forward(20)
