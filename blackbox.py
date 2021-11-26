import copy
from coordinate import Coordinate


class BlackBox:

    def __init__(self, position, callsign='default', heading=0):
        self.position = position
        self.callsign = callsign
        self.heading = heading

    @property
    def position(self):
        """getter method of position"""
        return self.__position

    @position.setter
    def position(self, position):
        """setter method of position and position must be Coordinate object"""
        if not isinstance(position, Coordinate):
            raise TypeError("position must be Coordinate object")
        self.__position = copy.deepcopy(position)

    @property
    def callsign(self):
        """getter method of callsign"""
        return self.__callsign

    @callsign.setter
    def callsign(self, callsign):
        """setter method of callsign and callsign must be string"""
        if not isinstance(callsign, str):
            raise TypeError("callsign must be string")
        self.__callsign = copy.deepcopy(callsign)

    @property
    def heading(self):
        """getter method of heading"""
        return self.__heading

    @heading.setter
    def heading(self, heading):
        """setter method o heading and heading must be number"""
        if not isinstance(heading, (int, float)):
            raise TypeError("heading must be number")
        self.__heading = copy.deepcopy(heading)

    def __repr__(self):
        """represent method for Blackbox class"""
        return f'Blackbox callsign={self.callsign}, position={self.position}, heading={self.heading}'
