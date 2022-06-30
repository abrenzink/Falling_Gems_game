class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def is_near(self, other):
        """Whether or not this Point is near to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are near; false if otherwise.
        """


        return self._x < other.get_x() + 5 and \
                self._x > other.get_x() - 5 and \
                self._y < other.get_y() + 15 and \
                self._y > other.get_y() - 15

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)