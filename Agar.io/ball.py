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
		self.r= r
		self.shape("circle")
		self.shapesize = self.r/10
		self.color(color)
	def move(self, width, height):
		self.width=width
		self.height=height
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy

		self.goto(new_x, new_y)

		right_side_ball= new_x + self.r
		left_side_ball= new_x - self.r
		top_side_ball= new_y + self.r
		bottom_side_ball= new_y - self.r


		if top_side_ball>= height/2:
			self.dy= -self.dy
			self.dx= -self.dx
		if bottom_side_ball <= -height/2:
			self.dy= -self.dy
			self.dx= -self.dx
		if right_side_ball <= -width/2:
			self.dy= -self.dy
			self.dx= -self.dx
		if left_side_ball >= (width/2):
			self.dy= -self.dy
			self.dx= -self.dx


ball1=Ball(0,0,3,1,100,"red")

while True:
	ball1.move(500,500)

turtle.mainloop()

