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
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]

tracer(1,0)
hideturtle()


for i in range(NUMBER_OF_BALLS):
	X=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH- MAXIMUM_BALL_RADIUS)
	y=random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MIXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color=(random.random(0,255), random.random(0,255), random.random(0,255))
	ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball)
	

def move_all_balls():
	for i in BALLS:
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))
	if(distance + 10 < ball_a.r +ball_b.r):
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
				X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
				Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
				while X_AXISSPEED or Y_AXISSPEED == 0:
					X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
					Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
				radius =random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = (random.random(),random.random(),random.random())
				if ball_a.r  > ball_b.r:
					ball_b.r = radius
					ball_b.goto(X_COORDINATE, Y_COORDINATE)
					ball_b.dx = X_AXISSPEED
					ball_b.dy = Y_AXISSPEED
					ball_b.color(color)
					ball_b.shapesize(ball_b.r/10)
					ball_a.r = ball_a.r+2
					ball_a.shapesize(ball_a.r/10)
				else:
					ball_a.r = radius
					ball_a.goto(X_COORDINATE, Y_COORDINATE)
					ball_a.dx = X_AXISSPEED
					ball_a.dy = Y_AXISSPEED
					ball_a.color(color)
					ball_a.shapesize(ball_a.r/10)
					ball_b.r = ball_b.r+2
					ball_b.shapesize(ball_b.r/10)


 

def check_myball_collision():
	for ball in BALLS:
		if collide(MY_BALL,ball) == True:
			ball_r4 = ball.r 
			my_ball_r4 = MY_BALL.r
			X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
			Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			while X_AXISSPEED and Y_AXISSPEED == 0:
				X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DY)
				Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			print(radius)

		 	color = (random.random(),random.random(),random.random())
			print(color)

			if my_ball_r4 > ball_r4:
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
				MY_BALL.r = radius
				MY_BALL.x = X_COORDINATE
				MY_BALL.y = Y_COORDINATE
				MY_BALL.goto(X_COORDINATE, Y_COORDINATE)
				MY_BALL.dx = X_AXISSPEED
				MY_BALL.dy = Y_AXISSPEED
				MY_BALL.color(color)
				MY_BALL.shapesize(MY_BALL.r/10)
				ball.r = ball.r + 2
				ball.shapesize(ball.r/10)

				return True

	return False		

def movearound(event):
	X = event.x - round(SCREEN_WIDTH)
	Y = round(SCREEN_HEIGHT) - event.y
	MY_BALL.goto(X,Y)

turtle.getcanvas().bind("<Motion>" , movearound)
turtle.listen()

while RUNNING == True:
	move_all_balls()
	check_all_balls_collision()

	if check_myball_collision() == True :
		RUNNING = False
	time.sleep(0.05)

turtle.mainloop()