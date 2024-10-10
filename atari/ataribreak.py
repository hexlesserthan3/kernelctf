import turtle as tr
import random
import time

MOVE_DIST = 10
COLOR_LIST = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
weights = [1, 2, 3]

class Paddle(tr.Turtle):
    def __init__(self):
        super().__init__()
        self.color('steel blue')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

    def move_left(self):
        self.backward(MOVE_DIST)

    def move_right(self):
        self.forward(MOVE_DIST)

class Ball(tr.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move_dist = MOVE_DIST
        self.y_move_dist = MOVE_DIST
        self.reset()

    def move(self):
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1
        if y_bounce:
            self.y_move_dist *= -1

    def reset(self):
        self.goto(x=0, y=-240)
        self.y_move_dist = 10

class Brick(tr.Turtle):
    def __init__(self, x_cor, y_cor, number):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLOR_LIST))
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(weights)
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15
        self.number = number
        self.revealed = False

    def reveal_number(self):
        if not self.revealed:
            self.revealed = True
            self.clear()
            self.write(str(self.number), align='center', font=('Arial', 12, 'normal'))

class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.numbers = [98, 114, 51, 97, 107, 95, 116, 104, 49, 115, 95, 103, 52, 109, 51, 95, 102, 48, 114, 95, 116, 104, 51, 95, 102, 108, 52, 103]
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-570, 570, 63):
            number = self.numbers.pop(0)  # Get the next number from the list
            brick = Brick(i, y_cor, number)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)

def check_collision_with_walls():
    

def check_collision_with_paddle():
    

def check_collision_with_bricks():
    global ball
    for brick in bricks.bricks:
        if (ball.xcor() > brick.left_wall and
            ball.xcor() < brick.right_wall and
            ball.ycor() > brick.bottom_wall and
            ball.ycor() < brick.upper_wall):
            ball.bounce(x_bounce=False, y_bounce=True)
            brick.reveal_number()
            bricks.bricks.remove(brick)
            break

screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()

playing_game = True

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)

while playing_game:
    screen.update()
    time.sleep(0.01)
    ball.move()
    check_collision_with_walls()
    check_collision_with_paddle()
    check_collision_with_bricks()

tr.mainloop()
