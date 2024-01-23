import turtle as tu

class Paddle(tu.Turtle):
    def __init__(self):
        super().__init__()
        # self.paddle= tu.Turtle() #this wont be needed as we are using class and sub-class

    def create_paddle(self, x,y,color1,shape1):
        # self.paddle.penup() #we do not need to use self.paddle any longer as we are using subclass in the constructor.
        self.penup()
        self.setx(x)
        self.sety(y)
        self.color(color1)
        self.shape(shape1)
        self.shapesize(5, 1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def down(self):
        self.goto(self.xcor(),self.ycor()-50)
        print(self.xcor(), self.ycor())






