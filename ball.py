import turtle as tu

class Ball(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.ball= tu.Turtle() #this wont be needed as we are using class and sub-class

#20 and 15. For every 20 x, 15 y is expected
# bouncing logic: 1) random right diagnol. 2) once at the edge, turn the heading, and move towards the right edge.
    #if touched by a paddle, again, go diagnoal on the opposite direction.

    def move(self):
        x= self.xcor()
        y=self.ycor()
        self.penup()
        self.goto(x+20,y+15)






