import turtle
from turtle import *

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r = r
		self.shape("circle")
		self.shapesize = self.r/10
		self.color(color)
	def move(self, width, height):
		
		current_x =self.xcor()
		new_x=self.xcor()+self.dx
		current_y= self.ycor()
		new_y=self.ycor()+self.dy
		right_side_ball= new_x+r
		left_side_ball=new_x-r
		top_side_ball=new_y+r
		top_side_ball=new_y-r
		


		self.goto(new_x,new_y)

ball1=Ball(0,0,0,2,100,"red")
ball1.goto(0,50)
ball1.move(100,100)

turtle.mainloop()

