import turtle


turtle.register_shape("shape_name", ((-25,0), (25,0), (25,50), (0,75),(-25,50),(-25,0)))
turtle.shape("shape_name")
turtle.right(90)



turtle.mainloop()