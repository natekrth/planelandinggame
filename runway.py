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
        self.turtle.pencolor('white')       # runway color is white
        self.turtle.hideturtle()
        self.turtle.shape('triangle')       # change turtle to be triangle symbol
        self.turtle.shapesize(0.8, 0.8, 0.8)  # change turtle size
        self.turtle.speed('fastest')

    @property
    def pos(self):
        """getter method of position"""
        return self.__pos

    @property
    def heading(self):
        """getter method of heading"""
        return self.__heading

    @property
    def width(self):
        """getter method of width"""
        return self.__width

    @property
    def length(self):
        """getter method of length"""
        return self.__length

    @pos.setter
    def pos(self, pos):
        """setter method position and position must be Coordinate object"""
        if not isinstance(pos, Coordinate):
            raise TypeError('pos must be a Coordinate')
        self.__pos = copy.deepcopy(pos)

    @heading.setter
    def heading(self, heading):
        """setter method heading and heading must be positive integer"""
        if not isinstance(heading, int):
            raise TypeError('heading must be integer')
        if heading < 0:
            raise ValueError('heading must be positive integer')
        self.__heading = copy.deepcopy(heading)

    @width.setter
    def width(self, width):
        """setter method width and width must be positive integer"""
        if not isinstance(width, int):
            raise TypeError('width must be integer')
        if width < 0:
            raise ValueError('width must be positive integer')
        self.__width = copy.deepcopy(width)

    @length.setter
    def length(self, length):
        """setter method length and length must be positive integer"""
        if not isinstance(length, int):
            raise TypeError('length must be integer')
        if length < 0:
            raise ValueError('length must be positive integer')
        self.__length = copy.deepcopy(length)

    def draw(self):
        """
        method draw will draw runway on the screen
        by given position, heading, length, and width using turtle
        """
        self.turtle.setheading(self.heading)
        for i in range(2):                      # draw runway
            self.turtle.forward(self.length)
            self.turtle.left(90)
            self.turtle.forward(self.width)
            self.turtle.left(90)
        self.turtle.left(90)
        self.turtle.forward(self.width/2)
        self.turtle.left(90)
        self.turtle.forward(self.length/1.5)   # draw ils approach line (shorter than runway)
        self.turtle.left(20)
        self.turtle.showturtle()

    def ils_data(self):
        """
        ils_data method return current ils x and y coordinate, and length of ils
        max heading and min heading both are data use for checking heading for capture ils
        check_top, check_bot, check_left, check_right are data use for checking position for capture ils
        """
        # ils length 1.5 times shorter than runway
        ils_length = self.length / 1.5

        # ils heading range Plus-Minus 20 degrees from ils's heading
        max_heading = self.heading + 20
        min_heading = self.heading - 20

        # ils'hitbox 1o distances away from ils's position x,y
        ils_x = self.turtle.xcor()
        ils_y = self.turtle.ycor()
        check_top = self.turtle.ycor() + 10
        check_bot = self.turtle.ycor() - 10
        check_left = self.turtle.xcor() - 10
        check_right = self.turtle.xcor() + 10
        return ils_x, ils_y, check_top, check_bot, check_left, check_right, self.heading, max_heading, min_heading, ils_length
