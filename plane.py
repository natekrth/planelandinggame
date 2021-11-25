from coordinate import Coordinate
from turtle import Turtle
from blackbox import BlackBox
from database import FlightDB
import time
import copy


class Plane:

    def __init__(self, callsign, heading ,pos, color='green'):
        self.callsign = callsign
        self.heading = heading
        self.pos = pos
        self.color = color
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.shapesize(2,2,2)
        self.turtle.speed('fastest')
        self.turtle.penup()
        self.blackbox = {}
        self.flight_data_dt = {}

    @property
    def callsign(self):
        return self.__callsign

    @property
    def heading(self):
        return self.__heading

    @property
    def pos(self):
        return self.__pos

    @property
    def color(self):
        return self.__color

    @callsign.setter
    def callsign(self, callsign):
        if not isinstance(callsign, str):
            raise TypeError('callsign must be a string')
        self.__callsign = copy.deepcopy(callsign)

    @heading.setter
    def heading(self, heading):
        if not isinstance(heading, int):
            raise TypeError('heading must be integer')
        if heading < 0:
            raise ValueError('heading must be positive integer')
        self.__heading = copy.deepcopy(heading)

    @pos.setter
    def pos(self, pos):
        if not isinstance(pos, Coordinate):
            raise TypeError('pos must be a Coordinate')
        self.__pos = copy.deepcopy(pos)

    @color.setter
    def color(self, color):
        """
        Setter method of color
        throwing a TypeError if color is not a string
        """
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        # set attribute color (private) to property
        self.__color = copy.deepcopy(color)  # deepcopy preventing changing original object

    def goto_start_position(self):
        self.turtle.hideturtle()
        self.turtle.color(self.color)
        self.turtle.goto(self.pos.x, self.pos.y)
        self.turtle.setheading(self.heading)
        self.turtle.showturtle()

    def forward(self, speed):
        self.turtle.forward(speed)

    def left(self):
        self.turtle.left(2)

    def right(self):
        self.turtle.right(2)

    def show_pos(self):
        return self.turtle.pos()

    def show_heading(self):
        return self.turtle.heading()

    def flight_data(self, dt):
        plane_cor = Coordinate(self.turtle.xcor(), self.turtle.ycor())
        data = BlackBox(plane_cor, self.callsign, self.turtle.heading())
        db = FlightDB("Data1")
        self.flight_data_dt[dt] = data
        self.blackbox[self.callsign] = self.flight_data_dt
        db.insert(self.callsign, self.flight_data_dt)
        # print(self.blackbox)

    def position_data(self, distance):
        check_top = self.turtle.ycor() + distance
        check_bot = self.turtle.ycor() - distance
        check_left = self.turtle.xcor() - distance
        check_right = self.turtle.xcor() + distance
        return check_top, check_bot, check_left, check_right

    def close_call(self):
        self.turtle.color('red')

    def normal_state(self, color):
        self.turtle.color(color)

    def approach(self, x, y, heading, length):
        self.turtle.goto(x, y)
        self.turtle.setheading(heading)
        print("Autopilot")
        for i in range(int(length)):
            self.turtle.forward(1)
            time.sleep(0.1)
        self.turtle.hideturtle()

    def clear(self):
        self.turtle.clear()

    def hide(self):
        self.turtle.hideturtle()

    def text(self):
        self.turtle.clear()
        if self.turtle.heading() < 150:
            self.turtle.write((self.__callsign, self.turtle.heading(), self.turtle.pos()), align='left', font=('Arial', 15, 'normal'))
        elif self.turtle.heading() >= 225:
            self.turtle.write((self.__callsign, self.turtle.heading(), self.turtle.pos()), align='left',
                              font=('Arial', 15, 'normal'))
        elif self.turtle.heading() >= 150:
            self.turtle.write((self.__callsign, self.turtle.heading(), self.turtle.pos()), align='right',
                              font=('Arial', 15, 'normal'))

