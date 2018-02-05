import turtle
import time
import random
import math
from ball import Ball 

turtle.tracer(delay=0)
turtle.hideturtle()

turtle.colormode(255)


SLEEP = 0.0077
SCREEN_WIDTH= round(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT= round(turtle.getcanvas().winfo_height()/2)
RUNNING= True 




NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

My_Ball=Ball(0,0,0,0,30,"red")

BALLS=[]



for i in range(NUMBER_OF_BALLS):
        x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
        y=random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
        dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
        dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
        radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
        color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball=Ball(x,y,dx,dy,radius,color)
        BALLS.append(ball)


def move_all_balls():
        for ball in BALLS:
                ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
        if ball_a==ball_b:
                return False
        distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))
        if distance + 10 < ball_a.r +ball_b.r:
                return True
        else:	
                return False

def check_all_balls_collision():
        for ball_a in (BALLS):
                for ball_b in (BALLS):
                        if collide(ball_a,ball_b)==True:
                                ball_a_radius=ball_a.r
                                ball_b_radius=ball_b.r	
                                X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                                Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                                dx = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
                                dy = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
                                while dx or dy == 0:
                                        dx = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
                                        dy = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
                                radius =random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
                                color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                                if ball_a.r  > ball_b.r:
                                        ball_b.r = radius
                                        ball_b.goto(X_COORDINATE, Y_COORDINATE)
                                        ball_b.dx = dx
                                        ball_b.dy = dy
                                        ball_b.color(color)
                                        ball_b.shapesize(ball_b.r/10)
                                        ball_a.r = ball_a.r+2
                                        ball_a.shapesize(ball_a.r/10)
                                else:
                                        ball_a.r = radius
                                        ball_a.goto(X_COORDINATE, Y_COORDINATE)
                                        ball_a.dx = dx
                                        ball_a.dy =dy
                                        ball_a.color(color)
                                        ball_a.shapesize(ball_a.r/10)
                                        ball_b.r = ball_b.r+2
                                        ball_b.shapesize(ball_b.r/10)




def check_myball_collision():
        for ball in BALLS:
                if collide(My_Ball,ball) == True:
                        a_rad = ball.r 
                        me_rad = My_Ball.r
                        X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                        Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                        dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
                        dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                        while dx and dy == 0:
                                dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DY)
                                dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

                        radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
                        color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))

                        if me_rad > a_rad:
                                ball.r = radius
                                ball.x = X_COORDINATE
                                ball.y = Y_COORDINATE
                                ball.goto(X_COORDINATE, Y_COORDINATE)
                                ball.dx = X_AXISSPEED
                                ball.dy = Y_AXISSPEED
                                ball.color(color)
                                ball.shapesize(ball.r/10)
                                MY_BALL.r = my_ball_r4 + 2
                                MY_BALL.shapesize(MY_BALL.r/10)
                        else:
                                return False

        return True	

def movearound(event):
        My_Ball.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>" , movearound)
turtle.listen()

while RUNNING == True:
        if (SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2):
                SCREEN_WIDTH=round(turtle.getcanvas().winfo_width()/2)
                SCREEN_HEIGHT=round(turtle.getcanvas().winfo_height()/2)
        move_all_balls()
        check_all_balls_collision()
        RUNNING = check_myball_collision()
        turtle.getscreen().update()
        turtle.update()
        time.sleep(SLEEP)
turtle.mainloop()
