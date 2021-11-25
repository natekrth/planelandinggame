from coordinate import Coordinate
import copy
import csv
from coordinate import Coordinate

class BlackBox:

    def __init__(self, position, callsign='default', heading=0):
        self.position = position
        self.callsign = callsign
        self.heading = heading

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, Coordinate):
            raise TypeError("position must be Coordinate object")
        self.__position = copy.deepcopy(position)

    @property
    def callsign(self):
        return self.__callsign

    @callsign.setter
    def callsign(self, callsign):
        if not isinstance(callsign, str):
            raise TypeError("callsign must be string")
        self.__callsign = copy.deepcopy(callsign)

    @property
    def heading(self):
        return self.__heading

    @heading.setter
    def heading(self, heading):
        if not isinstance(heading, (int, float)):
            raise TypeError("heading must be number")
        self.__heading = copy.deepcopy(heading)


    def __repr__(self):
        return f'Blackbox callsign={self.callsign}, position={self.position}, heading={self.heading}'

