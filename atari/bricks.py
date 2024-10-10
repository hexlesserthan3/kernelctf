from turtle import Turtle
import random

COLOR_LIST = ['light blue', 'royal blue', 
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue', 
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink', 
              'medium sea green', 'khaki']

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 
           3, 1, 1, 1, 4, 1, 3, 2, 2, 
           1, 2, 1, 2, 1, 2, 1]

RN = [98, 114, 51, 97, 107, 95, 116, 104, 
      49, 115, 95, 103, 52, 109, 51, 95, 
      102, 48, 114, 95, 116, 104, 51, 95, 
      102, 108, 52, 103]

class Brick(Turtle):
    def __init__(self, x_cor, y_cor, reveal_number=None):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLOR_LIST))
        self.goto(x=x_cor, y=y_cor)

        self.reveal_number = reveal_number  
        self.quantity = random.choice(weights)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15

    def hit(self):
        if self.reveal_number is not None:
            self.clear() 
            self.write(self.reveal_number, align="center", font=("Arial", 14, "normal")) 


class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor, reveal_numbers=None):
        for i, x_cor in enumerate(range(-570, 570, 63)):
            reveal_number = reveal_numbers[i] if reveal_numbers and i < len(reveal_numbers) else None
            brick = Brick(x_cor, y_cor, reveal_number=reveal_number)
            self.bricks.append(brick)

    def create_all_lanes(self):
        self.create_lane(self.y_start, reveal_numbers=RN)
        
        for y_cor in range(self.y_start + 32, self.y_end, 32):
            self.create_lane(y_cor)



