from turtle import Turtle,colormode
import random
import turtle



class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
	def random_color(self):
		colormode(255)
		r=random.randint(0,256)
		b=random.randint(0,256)
		g=random.randint(0,256)

		self.color(r,b,g)


a=Square(10)
a.random_color()

turtle.mainloop()


		
		