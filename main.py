import paddle as pad
import turtle as tu
import ball
import time

eog= False
ball_moving=True

screen1= tu.Screen()
screen1.bgcolor("black")
screen1.setup(800,600)
screen1.listen()
screen1.tracer(0)

pad_r=pad.Paddle()
pad_l=pad.Paddle()
ball1=ball.Ball()

pad_r.create_paddle(x=350,y=0,color1="white",shape1="square")
pad_l.create_paddle(x=-350,y=0,color1="pink",shape1="square")
screen1.onkey(pad_r.up,"Up")
screen1.onkey(pad_r.down,"Down")
screen1.onkey(pad_l.up,"w")
screen1.onkey(pad_l.down,"s")
while eog==False:
    screen1.update()
    ball1.move()
    time.sleep(0.1)

    if ball1.ycor() >= 290:#hits the top
        ball1.bounce_down()

    # if ball1.ycor() <= -290:#hits the bottom
    #     while ball1.ycor()
    #     ball1.bounce_up()
    #     ball1.move()

screen1.exitonclick()