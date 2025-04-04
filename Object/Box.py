import re
from .shape import Shape
from Vector3d import Vector3D

class Box(Shape):
    def __init__(self, x: float = 10.0, y: float = 10.0, z: float = 10.0):
        super().__init__("box")
        self._sides = Vector3D()

    def get_sides(self):
        return self._sides

    def set_sides(self, str):
        self._sides = Vector3D(str)

    def print_info(self):
        super().print_info()
        self._sides.print_info()
        