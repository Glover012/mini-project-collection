import turtle
import time
from food import *
from snake import *

win = turtle.Screen()
win.title("Snake game")

screenWidth = 1080
screenHeight = 720

win.setup(width=screenWidth, height=screenHeight)
win.bgcolor("#c2d37d")

snake = Snake(startX=0, startY= 0, screenWidth=screenWidth, screenHeight=screenHeight)
win.listen()

win.onkey(snake.keyUp, "Up")
win.onkey(snake.keyDown, "Down")
win.onkey(snake.keyLeft, "Left")
win.onkey(snake.keyRight, "Right")

win.onkey(snake.keyUp, "w")
win.onkey(snake.keyDown, "s")
win.onkey(snake.keyLeft, "a")
win.onkey(snake.keyRight, "d")

food = Food(screenWidth=screenWidth, screenHeight=screenHeight)

while True:
    win.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    if snake.checkSelfCollsion() or snake.checkWallsCollision():
        food.refresh()
        snake.refresh()

win.mainloop()
