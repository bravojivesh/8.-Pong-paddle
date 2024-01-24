import turtle as tu
import random

class Ball(tu.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.ball= tu.Turtle() #this wont be needed as we are using class and sub-class
        self.xsteps= random.randrange(20,30 ) #random so that it starts with a new angle everytime. Instructor only has 10. This is all me.
        self.ysteps = random.randrange(10, 20)  # same as above.
        #i spent a lot of time to understand this: if the values are huge, the xcord makes huge jumps.
        # So even if the distance is too near, it will keep moving as the xcor is good. Say, when in the near edge eg. 359, it will jump to 390.
        # and bounce will use the same steps with -ve. 31 becomes -31. Xcor will go back to 359, but the distance will be shorter nearer, and bounce logic will run again.
        #SEE SCRATCH FILE FOR LOG

        #solution: (see bounce_paddle method). I harcoded the location of the xcor for the ball.



        #the above two are variables I created and ARE NOT A PART OF CLASS TURTLE

#20 and 15. For every 20 x, 15 y is expected
# bouncing logic: 1) random right diagnol. 2) once at the edge, turn the heading, and move towards the right edge.
    #if touched by a paddle, again, go diagnoal on the opposite direction.

    def move(self):
        x= self.xcor()
        y=self.ycor()
        self.penup()
        self.goto(x + self.xsteps, y + self.ysteps)
        #this is not enough to say which direction, as it will always

        # self.goto(x + self.xsteps, y - self.ysteps) -- use this if you want the ball to go down in the beginning.

    def bounce(self):
        self.ysteps *= -1
        #simply changing the y- cor is enough. Because the rest will be handled by move method.
        # will work for both bouncing up and down. If the ycord is positive(going up), it becomes negative. If negative (going down), it becomes positive.

    def bounce_paddle(self):
        r = random.randrange(start=350,stop=360)
        if self.xcor() >0: #if on the right side
            self.setx(r)
        elif self.xcor() <0: #if on the left side
            self.setx(-r)

        self.xsteps *=-1 #steps reverse the direction

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_paddle()










