import turtle as tu

class Score(tu.Turtle):

    def __init__(self):
        super().__init__()
        self.count_r=0
        self.count_l=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display()
    def display(self):
        self.goto(50, 0)
        self.write(f"Score\n right:{self.count_r} ", False, align="center", font="Arial")

        self.goto(-50, 0)
        self.write(f"Score\n left:{self.count_l} ", False, align="center", font="Arial")

    def score_update(self,x_cor): #this will only be called if there is a miss. So I am only using one parameter.
        #if not right collision, it has to be left.
        self.clear()
        if x_cor > 360:
            self.count_l +=1
        else:
            self.count_r +=1
        self.display()

    def over(self): #only used with main.py (my version of the game)
        self.goto(0,-50)
        self.write("GAME OVER!!", False, align="center", font="Arial")


