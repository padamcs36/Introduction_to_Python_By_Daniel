import turtle

x1, y1 = eval(input("Enter the center of the circle x, y: "))
radius = eval(input("Enter radius of the circle: "))
x2, y2 = eval(input("Enter a point of x, y: "))

#draw the circle

turtle.penup() # pull the pen up
turtle.goto(x1, y1-radius)
turtle.pendown() #pull the pen down
turtle.circle(radius)

#Draw the point verifying wether point is inside the circle or outside the circle
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.begin_fill() #begin to fill color in a shape
turtle.color("black")
turtle.circle(5)
turtle.end_fill() #fill the shape

#Display the status
turtle.penup()
turtle.goto(x1 - 70, y1 - radius - 20) #Text is displayed at that points

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
if d <= radius:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")

turtle.hideturtle()
turtle.done()