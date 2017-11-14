import turtle as t
from random import randint
t = t.Turtle()

#Fill the screen with the turtle image!
t.rectangle(0,0,800,600,image="turtle.png")

#Let's tell turtle to start drawing!
t.penDown()

#while True: is the same as saying "repeat the following forever".
while True:
    #Move turtle forward a random amount.
    t.moveForward(randint(0,50))
    #Turn turtle a random amount.
    t.turnRight(randint(10,20))
    #Change the draw color to a random color
    t.color((randint(0,255),randint(0,255),randint(0,255)))
