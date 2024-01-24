import turtle as tu

class Score(tu.Turtle):

    def __init__(self):
        super().__init__()
        self.count=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display()
    def display(self):
        self.goto(0,0)
        self.write(f"Score:{self.count} ", False, align="center", font="Arial")

    def score_update(self):
        self.count+=1
        self.clear()
        self.display()

    def over(self): #only used with main.py (my version of the game)
        self.goto(0,-50)
        self.write("GAME OVER!!", False, align="center", font="Arial")


