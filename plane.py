from coordinate import Coordinate
from turtle import Turtle
from blackbox import BlackBox
from database import FlightDB
import time
import copy


class Plane:

    def __init__(self, callsign, heading, pos, color='green'):
        self.callsign = callsign
        self.heading = heading
        self.pos = pos
        self.color = color
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.shapesize(2, 2, 2)
        self.turtle.speed('fastest')
        self.turtle.penup()
        self.blackbox = {}          # black box dictionary key:callsign, value:flight_data_dt dictionary
        self.flight_data_dt = {}    # flight data dictionary key:time, value:Blackbox object

    @property
    def callsign(self):
        """getter method of callsign"""
        return self.__callsign

    @property
    def heading(self):
        """getter method of heading"""
        return self.__heading

    @property
    def pos(self):
        """getter method of position"""
        return self.__pos

    @property
    def color(self):
        """getter method of color"""
        return self.__color

    @callsign.setter
    def callsign(self, callsign):
        """setter method of callsign and callsign must be string"""
        if not isinstance(callsign, str):
            raise TypeError('callsign must be a string')
        self.__callsign = copy.deepcopy(callsign)

    @heading.setter
    def heading(self, heading):
        """setter method of heading and heading must be positive number"""
        if not isinstance(heading, (int, float)):
            raise TypeError('heading must be number')
        if heading < 0:
            raise ValueError('heading must be positive number')
        self.__heading = copy.deepcopy(heading)

    @pos.setter
    def pos(self, pos):
        """setter method of pos and pos must be coordinate object"""
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
        """plane will go to start position"""
        self.turtle.hideturtle()
        self.turtle.color(self.color)               # set color of the plane
        self.turtle.goto(self.pos.x, self.pos.y)    # go to start position
        self.turtle.setheading(self.heading)        # set heading of the plane
        self.turtle.showturtle()

    def forward(self, speed):
        """
        method forward plane will go forward by given speed
        :param speed: speed of the plane (integer)
        """
        self.turtle.forward(speed)

    def left(self):
        """method turn left by 2 degree"""
        self.turtle.left(2)

    def right(self):
        """method turn right by 2 degree"""
        self.turtle.right(2)

    def show_pos(self):
        """method return position x and position y of a plane"""
        return self.turtle.pos()

    def show_heading(self):
        """method return heading of the plane in degree"""
        return self.turtle.heading()

    def flight_data(self, dt):
        """
        method flight_data will save flight data in the BlackBox object then create database and insert
        callsign and flight_data_dt dictionary into database
        :param dt: real time
        """
        plane_cor = Coordinate(self.turtle.xcor(), self.turtle.ycor())          # create Coordinate object
        data = BlackBox(plane_cor, self.callsign, self.turtle.heading())        # create Blackbox object
        db = FlightDB("Data1")                                                  # create database
        self.flight_data_dt[dt] = data                         # put key:time, value: Blackbox
        self.blackbox[self.callsign] = self.flight_data_dt       # put key:callsign, value:flight_data_dt dict
        db.insert(self.callsign, self.flight_data_dt)            # insert to database
        print(self.flight_data_dt)

    def position_data(self, distance):
        """
        method find hit box of the plane using top y-coordinate, bottom y-coordinate, far left x-coordinate,
        far right x-coordinate
        :param distance: distance from plane to the hit box
        """
        check_top = self.turtle.ycor() + distance               # check top y- coordinate of
        check_bot = self.turtle.ycor() - distance               # check bottom y-coordinate of plane's hit box
        check_left = self.turtle.xcor() - distance              # check left x-coordinate of plane's hit box
        check_right = self.turtle.xcor() + distance             # check right x-coordinate of plane's hit box
        return check_top, check_bot, check_left, check_right

    def close_call(self):
        """change color of the plane to red"""
        self.turtle.color('red')

    def normal_state(self, color):
        """change color of the plane to given color"""
        self.turtle.color(color)

    def approach(self, x, y, heading, length):
        """
        method that will start approach plane to the runway for landing
        :param x: x-coordinate of ils
        :param y: y-coordinate of ils
        :param heading: heading of runway
        :param length: length of ils
        """
        self.turtle.goto(x, y)                     # goto start point of the approach(ils)
        self.turtle.setheading(heading)            # set heading of the plane for the approach(ils)
        print("Autopilot")
        for i in range(int(length)):               # start approach to the runway
            self.turtle.forward(1)
            time.sleep(0.1)
        self.turtle.hideturtle()                   # after finish approach will hide turtle

    def clear(self):
        """clear text on the screen"""
        self.turtle.clear()

    def hide(self):
        """hide plane on the screen"""
        self.turtle.hideturtle()

    def text(self):
        """
        write flight data on the screen
        1.callsign
        2.heading of the plane
        3.position of the plane
        """
        self.clear()   # clear previous text on screen
        flight_data = (self.__callsign, self.turtle.heading(), self.turtle.pos())
        # change align of the text depend on heading of the plane (avoiding text overlap plane)
        if self.turtle.heading() < 150:
            self.turtle.write(flight_data, align='left', font=('Arial', 15, 'normal'))
        elif self.turtle.heading() >= 225:
            self.turtle.write(flight_data, align='left', font=('Arial', 15, 'normal'))
        elif self.turtle.heading() >= 150:
            self.turtle.write(flight_data, align='right', font=('Arial', 15, 'normal'))
