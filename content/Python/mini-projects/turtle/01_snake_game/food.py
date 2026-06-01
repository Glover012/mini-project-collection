from turtle import Turtle
import random

class Food(Turtle):
    "Food class"
    def __init__(self, screenWidth, screenHeight):
        Turtle.__init__(self)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        shape = random.choice(["square", "circle", "triangle"])
        color = random.choice(["orange", "blue", "red"])
        self.hideturtle()
        self.shape(shape)
        self.color(color)

        widthX = int(self.screenWidth/2) - 20
        heightY = int(self.screenHeight/2) - 20
        randomPossitionX = random.randint( widthX*-1, widthX )
        randomPossitionY = random.randint( heightY*-1, heightY )
        self.goto( randomPossitionX, randomPossitionY )
        self.showturtle()
