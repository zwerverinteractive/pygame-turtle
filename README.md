'''

	#This program gives you a basic turtle to play around with.
	#A simple, uncomplicated playground for learning python.
	#I wrote it for my girlfriend.
	#It is build on pygame, so you'll need to install that in addition to python. 
	#Use your favourite seach engine to find out how to do that!


	from turtle import Turtle
	turtle = Turtle()

	turtle.hide()			#Turtle will turn invisible!
	turtle.show()			#Turtle is no longer invisible.

	turtle.moveForward(20)		#Turtle will move forward 20 pixels.
	turtle.moveBackward(6)		#Turtle will move backward 6 pixels.
	turtle.moveLeft(64)		#Turtle will strafe to the left for 64 pixels.
	turtle.moveRight(12)		#Turtle will strafe to the left for 12 pixels.
	turtle.turnLeft(10)		#Turtle will rotate 10 degrees to the left.
	turtle.turnRight(180)		#Turtle will rotate 180 degrees to the right
	turtle.teleport(20, 50)		#Turtle will teleport to 20 pixels from the left and 50 pixels from the top.

	turtle.penDown()		#Turtle will start drawing lines.
	turtle.penUp()			#Turtle will stop drawing lines.
	turtle.width(4)			#Turtle will draw lines 4 lines wide.
	turtle.color((127,255,127))	#Turtle sets the drawing color to a bright green.
	turtle.fill((0,0,0))		#Turtle fills the entire screen with black.

	turtle.rectangle(23, 46, 50, 100, (64,0,0))
	#Turtle draws a rectangle.
	#It is located 23 pixels from the right and 46 pixels from the top.
	#It is 50 pixels wide and 100 pixels tall.
	#It is dark red.
	
	turtle.rectangle(0, 6, 32, 32, image="turtle.png")
	#Turtle draws an image of a turtle.
	#It is located 0 pixels from the right and 6 pixels from the top.
	#It is 32 pixels wide and 32 pixels tall.
	#Add more images in the same folder as turtle to acces them!
		

'''
