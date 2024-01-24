import turtle as tu

class Score(tu.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,30)
        self.color("white")
        self.write(f"Score: ", False, align="center", font="Arial")