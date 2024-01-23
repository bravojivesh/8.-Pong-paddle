import turtle as tu
import random

class Ball(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.ball= tu.Turtle() #this wont be needed as we are using class and sub-class
        self.xsteps= random.randrange(10, 30)
        self.ysteps=random.randrange(10, 30)
        #the above two are variables I created and ARE NOT A PART OF CLASS TURTLE

#20 and 15. For every 20 x, 15 y is expected
# bouncing logic: 1) random right diagnol. 2) once at the edge, turn the heading, and move towards the right edge.
    #if touched by a paddle, again, go diagnoal on the opposite direction.

    def move(self):
        x= self.xcor()
        y=self.ycor()
        self.penup()
        self.goto(x + self.xsteps, y + self.ysteps)

    def move_down(self):
        x = self.xcor()
        y = self.ycor()
        self.penup()
        self.goto(x + self.xsteps, y - self.ysteps)
    def bounce_down(self):
        self.ysteps *= -1
        #simply changing the y- cor is enough. Becuase the rest will be handled by move method.

    def bounce_up(self):
        self.ysteps= abs(self.ysteps)
        #still working on how to move the ball upwards. What should we call? move or a separate method is needed?









