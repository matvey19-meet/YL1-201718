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
		self.width=width
		self.height=height
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy

		right_side_ball= new_x + self.r
		left_side_ball= new_x - self.r
		top_side_ball= new_y + self.r
		bottom_side_ball= new_y - self.r


		if top_side_ball>= height/2:
			new_y=current_y
		if bottom_side_ball <= -(height/2):
			new_y=current_y
		if right_side_ball <= width/2:
			new_x=current_x
		if left_side_ball >= -(width/2):
			new_x=current_x



		self.goto(new_x,new_y)

ball1=Ball(0,0,1,0,100,"red")
# ball1.goto(0,100)
while True:
	ball1.move(100,100)

turtle.mainloop()

