# This is a simple pong game that created by using graphics.py
from graphics import *
from random import choice

# Setting window
win = GraphWin("Pong Game", 600, 300)
win.setCoords(0, 0, 600, 300)
win.setBackground("black")

# Creating ball and paddles
ball = Circle(Point(300, 150), 10)
ball.setFill("white")
ball.draw(win)
leftPaddle = Rectangle(Point(5, 120), Point(15, 180))  # width 10 height 60
leftPaddle.setFill("white")
leftPaddle.draw(win)
rightPaddle = Rectangle(Point(585, 120), Point(595, 180))
rightPaddle.setFill("white")
rightPaddle.draw(win)

# Score Board
leftScore = 0  # Variables to store scores
rightScore = 0
leftScoreText = Text(Point(290, 280), str(leftScore)+" |")
leftScoreText.setSize(25)
leftScoreText.setFill("white")
leftScoreText.draw(win)
rightScoreText = Text(Point(310, 280), "    "+str(rightScore))
rightScoreText.setFill("white")
rightScoreText.setSize(25)
rightScoreText.draw(win)

# Variables for directions
directions = [1, -1]
xDirection = choice(directions)
yDirection = choice(directions)


def movement(key):
    # Fnc to move paddles
    if key == "w":
        if leftPaddle.getCenter().getY()+30 >= 300:
            pass
        else:
            leftPaddle.move(0, 20)
    if key == "s":
        if leftPaddle.getCenter().getY() - 30 <= 0:
            pass
        else:
            leftPaddle.move(0, -20)
    if key == "8":
        if rightPaddle.getCenter().getY() + 30 >= 300:
            pass
        else:
            rightPaddle.move(0, 20)
    if key == "2":
        if rightPaddle.getCenter().getY() - 30 <= 0:
            pass
        else:
            rightPaddle.move(0, -20)


def delay(s):
    # This function is to control the speed of the ball
    for i in range(s):
        for j in range(1000):
            pass


def bounce():
    # Fnc to bounce the ball
    global yDirection, xDirection, leftScore, rightScore
    x = ball.getCenter().getX()  # Coordinate for ball
    y = ball.getCenter().getY()
    rpx = rightPaddle.getCenter().getX()  # Coordinate for right paddle
    rpy = rightPaddle.getCenter().getY()
    lpx = leftPaddle.getCenter().getX()  # Coordinate for left paddle
    lpy = leftPaddle.getCenter().getY()
    if y+10 >= 300:
        yDirection = -1
    if y-10 <= 0:
        yDirection = 1
    if (x >= (rpx-15)) and (rpy-30 <= y <= rpy+30):
        xDirection = -1
    if (x <= (lpx+15)) and (lpy-30 <= y <= lpy+30):
        xDirection = 1
    if x >= 600:
        leftScore += 1
        leftScoreText.setText(str(leftScore)+" |")
        ball.undraw()
        ball.p1.x = 290
        ball.p2.x = 310
        ball.draw(win)
    if x <= 0:
        rightScore += 1
        rightScoreText.setText("    "+str(rightScore))
        ball.undraw()
        ball.p1.x = 290
        ball.p2.x = 310
        ball.draw(win)


def game_over():
    # Fnc to determine winner
    global end_game
    if leftScore == 5:
        last_text = Text(Point(300, 150), "Left Player Won!")
        last_text.setSize(30)
        last_text.setFill(color_rgb(255, 215, 0))
        ball.undraw()
        leftPaddle.undraw()
        rightPaddle.undraw()
        last_text.draw(win)
        end_game = True

    if rightScore == 5:
        last_text = Text(Point(300, 150), "Right Player Won!")
        last_text.setSize(30)
        last_text.setFill(color_rgb(255, 215, 0))
        ball.undraw()
        leftPaddle.undraw()
        rightPaddle.undraw()
        last_text.draw(win)
        end_game = True
    if end_game:
        win.getMouse()
        win.close()


end_game = False
while True:
    if end_game:
        break
    game_over()
    d = 800  # The speed of the ball
    delay(d)  # Fnc that controls the ball movement speed
    ball.move(xDirection, yDirection)  # Moving ball
    bounce()  # Bouncing ball
    Movement = ""
    try:
        Movement = win.checkKey()  # Checking for user's paddle commands
    except GraphicsError:
        pass
    movement(Movement)  # Moving Paddles
