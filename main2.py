#MAIN2 IS THE INSTRUCTOR'S VERSION.
# POINT WHEN THE OPPONENT MISSES.
# RESET THE BALL AND GIVE THE OTHER PLAYER THE FIRST CHANCE TO PADDLE

import paddle as pad
import score2
import turtle as tu
import ball
import time

eog= False
ball_moving=True

screen1= tu.Screen()
score1=score2.Score()

screen1.bgcolor("black")
screen1.setup(800,600)
screen1.listen()
screen1.tracer(0)

pad_r=pad.Paddle()
pad_l=pad.Paddle()
ball1=ball.Ball()

pad_r.create_paddle(x=380,y=0,color1="white",shape1="square")
pad_l.create_paddle(x=-380,y=0,color1="pink",shape1="square")
screen1.onkey(pad_r.up,"Up")
screen1.onkey(pad_r.down,"Down")
screen1.onkey(pad_l.up,"w")
screen1.onkey(pad_l.down,"s")

while eog==False and ball1.xcor()<400 and ball1.xcor() >-400:
    screen1.update()
    ball1.move()
    time.sleep(0.2)
    distance= ball1.distance(pad_r)
    distance1=ball1.distance(pad_l)
    # print (f"distance to paddle_r is: {distance}, pad_l distance: {distance1} and ball xcord is {ball1.xcor()}\n the xsteps is {ball1.xsteps}\n ysteps is {ball1.ysteps}")

    if ball1.ycor() > 290 or ball1.ycor() <-290: #hits the top or bottom
        ball1.bounce()

    if (ball1.distance(pad_r) <50 and ball1.xcor() >350) or (ball1.distance(pad_l)<50 and ball1.xcor() < -350):
        # when hits the paddle
        #db: print ("*****BOUNCE*********")
        ball1.bounce_paddle()

    elif ball1.xcor()>360 or ball1.xcor() <-360: #out of bound
        # db:print (ball1.xcor())
        score1.score_update(ball1.xcor())
        ball1.reset_pos()
        #because the sequence of the above two lines were wrong, my score_update method was NOT working.
        # db:print(score1.count_l, score1.count_r)




screen1.exitonclick()