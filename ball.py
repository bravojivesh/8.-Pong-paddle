import turtle as tu
import random

class Ball(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.ball= tu.Turtle() #this wont be needed as we are using class and sub-class
        self.xsteps= random.randrange(10, 30) #random so that it starts with a new angle everytime. Instructor only has 10. This is all me.
        self.ysteps=random.randrange(10, 30) #same as above.
        #the above two are variables I created and ARE NOT A PART OF CLASS TURTLE

#20 and 15. For every 20 x, 15 y is expected
# bouncing logic: 1) random right diagnol. 2) once at the edge, turn the heading, and move towards the right edge.
    #if touched by a paddle, again, go diagnoal on the opposite direction.

    def move(self):
        x= self.xcor()
        y=self.ycor()
        self.penup()
        self.goto(x + self.xsteps, y + self.ysteps)
        # self.goto(x + self.xsteps, y - self.ysteps) -- use this if you want the ball to go down in the beginning.

    def bounce(self):
        self.ysteps *= -1
        #simply changing the y- cor is enough. Because the rest will be handled by move method.
        # will work for both bouncing up and down. If the ycord is positive(going up), it becomes negative. If negative (going down), it becomes positive.

    def bounce_paddle(self):
        if self.xcor()>360 or self.xcor()< -360:
            self.xsteps=-50
            #Writing this if/else: Because I have random vales for x and y stemps, sometimes the ball is too close to the paddle even after bouncing for the "first time". So it bounces again, coz it meets
            # both conditions for bouncing in main.py, i.e., x cor is too close to the edge and distance with paddle is too close.
        else:
            self.xsteps = (random.randrange(10, 30)) * -1
            #now becuase of if/else, the above is not working for left paddle










