#!/usr/bin/python3
"""
Define a Rectangle class that inherits from Base.
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherited from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier for each instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position (default is 0).
            y (int, optional): The y-coordinate of the rectangle's position (default is 0).
            id (int, optional): The unique identifier for the instance (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width.
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width.
        
        Args:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter fn for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter function for x.

        Args:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y.
        Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y.

        Args:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """Print a visual representation of the rectangle using '#' characters."""
        map_str = ""
        symbol = "#"

        print("\n" * self.__y, end="")

        for i in range(self.__height):
            map_str += (" " * self.__x) + (symbol * self.__width) + "\n"
        print(map_str, end="")

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Positional arguments (id, width, height, x, y).
            **kwargs: Keyword arguments.

        Notes:
            If positional arguments are present, keyword arguments are ignored.
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle object.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'x': getattr(self, "x"),
            'y': getattr(self, "y"),
            'id': getattr(self, "id"),
            'height': getattr(self, "height"),
            'width': getattr(self, "width")
        }

