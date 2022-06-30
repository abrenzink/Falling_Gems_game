import random

from game.casting.actor import Actor
from game.shared.point import Point

class Gems(Actor):
    """
    a precious or semiprecious stone.
    
    The responsibility of Gems is to give or remove player's points.

    Attributes:
        _points (int): the value of each gem.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def get_points(self):
        """Gets the gem's points.
        
        Returns:
            int: the number of points.
        """
        return self._points
    
    def set_points(self):
        """Defines how many points this particular gem has."""

        if (self._text == "*"):
            self._points = self._points + 1
        else:
            self._points = self._points - 1
    
    def make_fall(self, max_y):
        """Let gems fall from the sky. Will wrap the position from one side of the 
            screen to the other when it reaches the given maximum x and y values.

        Args:
            max_y (int): The maximum y value.
        """
        x = self.get_position().get_x()
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def reset_position(self):
        """Once a gem is collected and player score is updated, makes the collected
            gem be reloaded at the top of the screen with a new Y velocity.
        """
        
        x = random.randint(1, 60 - 1)
        vel_y = random.randint(5, 12)
        self._velocity = Point(0, vel_y)
        self._position = Point(x, 0).scale(15)