"""Making and Testing Points!"""
from __future__ import annotations

__author__ = "730671788"


class Point: 
    """Defining Point!"""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """INIT function reassigning x and y to an an intial value."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Sclae_by Mutating functions."""
        self.x = self.x * factor
        self.y = self.y * factor
    
    def scale(self, factor: int) -> Point:
        """Returning new point."""
        new_point: Point = Point(self.x, self.y)
        new_point.x = new_point.x * factor
        new_point.y = new_point.y * factor
        return new_point