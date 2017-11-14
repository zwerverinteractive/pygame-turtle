#Hello! This is the turtle class. You can tweak it if you like!

import pygame
from sys import exit
import math as Math
pygame.init()
screen=pygame.display.set_mode((800,600),0,32)
drawscreen=pygame.Surface((800,600))
turtlescreen=pygame.Surface((800,600))
turtlescreen.set_colorkey((0,255,0))
clock = pygame.time.Clock()

pygame.display.set_caption("Turtle!")
turtle = pygame.image.load('turtle.png')
turtle.set_colorkey((0,255,0))
pygame.display.set_icon(turtle)

class Turtle:
    def __init__(self, x=400, y=300):
        self.img = pygame.Surface((32,32))
        self.img.fill((0,255,0))
        self.img.set_colorkey((0,255,0))
        self.img.blit(turtle, (0,0))

        self.x = x
        self.y = y
        self.speed = 1
        self.angle = 0
        self.pen = "up"
        self.current_color = (128,255,128)
        self.lineWidth = 1
        self.bgColor = (0,0,0)
        self.timer = 0
        self.hidden = False
        self.images = {}
        self.update()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


        self.timer += 1
        if self.timer == self.speed:
            clock.tick()
            self.timer = 0
            screen.fill((0,0,0))
            screen.blit(drawscreen,(0,0))
            if not self.hidden:
                turtlescreen.fill((0,255,0))
                turtlescreen.blit(self.rot_center(self.img,self.angle), (self.x-16,self.y-16))
                screen.blit(turtlescreen, (0,0))
            pygame.display.flip()

    def hide(self):
        if self.hidden:
            print("Already hidden.")
        else:
            self.hidden = True

    def show(self):
        if not self.hidden:
            print("Already showing.")
        else:
            self.hidden = False

    def move(self, angle=0):
        x1 = self.x
        y1 = self.y
        self.x -= Math.sin(Math.radians(self.angle+angle))
        self.y -= Math.cos(Math.radians(self.angle+angle))
        if self.pen == "down":
            pygame.draw.line(drawscreen, self.current_color, (x1,y1), (self.x, self.y), self.lineWidth)

    def moveForward(self, amount=1):
        for i in range(amount):
            self.move()
            self.update()

    def moveBackward(self, amount=1):
        for i in range(amount):
            self.move(180)
            self.update()

    def moveLeft(self, amount=1):
        for i in range(amount):
            self.move(90)
            self.update()

    def moveRight(self, amount=1):
        for i in range(amount):
            self.move(270)
            self.update()

    def teleport(self, x, y):
        self.x = x
        self.y = y
        self.update()

    def turnLeft(self, amount=1):
        for i in range(amount):
            self.angle += 1
            if self.angle < 0:
                self.angle = 359
            self.update()

    def turnRight(self,amount=1):
        for i in range(amount):
            self.angle -= 1
            if self.angle > 359:
                self.angle = 0
            self.update()

    def penDown(self):
        if self.pen == "down": print("Pen is already down!")
        else: self.pen = "down"
        self.update()

    def penUp(self):
        if self.pen == "up": print("Pen is already up!")
        else: self.pen = "up"
        self.update()

    def color(self,color=(255,255,255)):
        self.current_color = color
        self.update()

    def width(self, width=1):
        self.lineWidth = width

    def fill(self, color=None):
        if color == None:
            drawscreen.fill(self.current_color)
        else:
            drawscreen.fill(color)

    def rectangle(self, x, y , w, h, image=None):
        if image == None:
            pygame.draw.rectangle(drawscreen, self.current_color, (x,y,w,h))
        else:
            if not image in self.images:
                self.images[image] = pygame.image.load(image)
            drawscreen.blit(pygame.transform.scale(self.images[image], (w, h)), (x,y))

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
