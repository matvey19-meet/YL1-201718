import turtle
import time
import random
from ball import Ball 

turtle.tracer(0)
hideturtle.turtle()

SLEEP = 0.0077
SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2
RUNNING= True 



NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX to = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]


for i in range(NUMBER_OF_BALLS):
	X=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH- MAXIMUM_BALL_RADIUS)
	y=random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MIXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color=(random.random(0,255), random.random(0,255), random.random(0,255))
	ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball)

for i in BALLS:
	ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)


def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	D = math.sqrt(math.pow((ball_b(x)-ball_a(x)),2) + math.pow((ball_b(y)-ball_a(y)),2))
	


