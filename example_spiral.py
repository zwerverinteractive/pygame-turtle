import turtle

turtle = turtle.Turtle()

turtle.penDown()
turtle.teleport(10,10)
turtle.speed = 20

for i in range(15):
	o = i*40
	turtle.turnRight(90)
	turtle.moveForward(780-o)
	turtle.turnRight(90)
	turtle.moveForward(580-o)
	turtle.turnRight(90)
	turtle.moveForward(780-o)
	turtle.turnRight(90)
	turtle.moveForward(560-o)

