from turtle import *
import random
from dist_formula import * 
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)



def check_collision(ball, ball2):
	x1=ball.xcor()
	y1=ball.ycor()
	x2=ball2.xcor()
	y2=ball2.ycor()
	d = dist_for(x1,y1,x2,y2)
	if(d>=0.0):
		ball=Ball.color("red")
		ball2=Ball.color("yellow")

ball= Ball(1,"black",1)
ball2=Ball(1,"green",1)
ball.goto(50,0)
ball2.goto(-50,0)

check_collision(ball,ball2)


turtle.mainloop()


