from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def point_to_left(self):
        self.l_score += 1
        self.refresh()

    def point_to_right(self):
        self.r_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.setpos(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))