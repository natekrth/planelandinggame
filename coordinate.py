import copy


class Coordinate:
    """Define a coordinate in 2D space."""

    def __init__(self, x=0, y=0):
        """
        Initialize a coordinate with the given x and y
        Default value of x is 0 and y is 0
        :param x: int or float
        :param y: int or float
        """
        self.x = copy.copy(x)
        self.y = copy.copy(y)

    @property
    def x(self):
        """getter methods of x"""
        return self.__x

    @property
    def y(self):
        """getter methods of y"""
        return self.__y

    @x.setter
    def x(self, x):
        """Setter method of x and throwing a TypeError if x is not a number"""
        if not isinstance(x, (int, float)):
            raise TypeError("The x attribute must be a number")
        # set attribute x (private) to property
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter method of x and throwing a TypeError if y is not a number"""
        if not isinstance(y, (int, float)):
            raise TypeError("The y attribute must be a number")
        # set attribute y (private) to property
        self.__y = y

    def __repr__(self):
        """
        Represent method for Coordinate
        :return: string
        """
        return f"Coordinate(x={self.x}, y={self.y})"
