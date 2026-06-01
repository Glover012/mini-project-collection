import turtle

class Snake:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    MOVE_DISTANCE = 20

    def __init__(self, startX, startY, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.startX = startX
        self.startY = startY
        self.segments = []
        self.refresh()

    def refresh(self):
        print("Snake reset")
        for seg in self.segments:
            seg.goto(3000,3000)
        self.segments.clear()

        self.segments = []
        self.addSegment(self.startX, self.startY)
        self.head = self.segments[0]
        self.direction = None
        
    def addSegment(self, x, y):
        t = turtle.Turtle("square")
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.goto(x,y)
        t.color("green")
        t.showturtle()
        self.segments.append(t)

    def extend(self):
        self.addSegment(3000, 3000)

    def keyUp(self):
        self.direction = Snake.UP

    def keyDown(self):
        self.direction = Snake.DOWN

    def keyLeft(self):
        self.direction = Snake.LEFT

    def keyRight(self):
        self.direction = Snake.RIGHT

    def move(self):
        headX = self.head.xcor()
        headY = self.head.ycor()

        if self.direction == Snake.UP:
            headY += Snake.MOVE_DISTANCE
        if self.direction == Snake.DOWN:
            headY -= Snake.MOVE_DISTANCE
        if self.direction == Snake.LEFT:
            headX -= Snake.MOVE_DISTANCE
        if self.direction == Snake.RIGHT:
            headX += Snake.MOVE_DISTANCE

        index = len(self.segments)-1
        while index > 0:
            newX = self.segments[index - 1].xcor()
            newY = self.segments[index - 1].ycor()
            self.segments[index].goto(newX, newY)
            index -= 1

        self.head.goto(headX, headY)

    def checkSelfCollsion(self):
        for seg in self.segments:
            if seg == self.head:
                continue
            elif self.head.distance(seg) < 20:
                return True
        return False
    
    def checkWallsCollision(self):
        halfWidth = self.screenWidth/2
        halfHeight = self.screenHeight/2
        x = self.head.xcor()
        y = self.head.ycor()

        if x > halfWidth or x < -halfWidth or y > halfHeight or y < -halfHeight:
            return True
