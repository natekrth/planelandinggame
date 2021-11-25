from coordinate import Coordinate
from turtle import Turtle
import copy

class Runway:

    def __init__(self, pos, heading, width, length):
        self.pos = pos
        self.heading = heading
        self.width = width
        self.length = length
        self.turtle = Turtle()
        self.turtle.pensize(2)
        self.turtle.pencolor('white')
        self.turtle.hideturtle()
        self.turtle.shape('triangle')
        self.turtle.shapesize(0.8,0.8,0.8)
        self.turtle.speed('fastest')
        self.__ils_pos_list = []


    @property
    def pos(self):
        return self.__pos

    @property
    def heading(self):
        return self.__heading

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @pos.setter
    def pos(self, pos):
        if not isinstance(pos, Coordinate):
            raise TypeError('pos must be a Coordinate')
        self.__pos = copy.deepcopy(pos)

    @heading.setter
    def heading(self, heading):
        if not isinstance(heading, int):
            raise TypeError('heading must be integer')
        if heading < 0:
            raise ValueError('heading must be positive integer')
        self.__heading = copy.deepcopy(heading)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be integer')
        if width < 0:
            raise ValueError('width must be positive integer')
        self.__width = copy.deepcopy(width)

    @length.setter
    def length(self, length):
        if not isinstance(length, int):
            raise TypeError('length must be integer')
        if length < 0:
            raise ValueError('length must be positive integer')
        self.__length = copy.deepcopy(length)

    def draw(self):
        self.turtle.setheading(self.heading)
        for i in range(2):
            self.turtle.forward(self.length)
            self.turtle.left(90)
            self.turtle.forward(self.width)
            self.turtle.left(90)
        self.turtle.left(90)
        self.turtle.forward(self.width/2)
        self.turtle.left(90)
        self.turtle.forward(self.length/1.5)
        self.turtle.left(20)
        self.turtle.showturtle()


    def ils_data(self):
        ils_x = self.turtle.xcor()
        ils_y = self.turtle.ycor()
        ils_length = self.length / 1.5
        max_heading = self.heading + 20
        min_heading = self.heading - 20
        check_top = self.turtle.ycor()+10
        check_bot = self.turtle.ycor()-10
        check_left = self.turtle.xcor()-10
        check_right = self.turtle.xcor()+10
        return ils_x, ils_y, check_top, check_bot, check_left, check_right, self.heading, max_heading, min_heading, ils_length




