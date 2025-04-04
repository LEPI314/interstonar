import re
from Object.shape import Shape
from Vector3d import Vector3D

class Body:

    def __init__(self, name: str = "Unnamed", position: str = None, direction: str = None, shape: Shape = None):
        self._name = name
        self._position = Vector3D(position) if position is not None else Vector3D()
        self._direction = Vector3D(direction) if direction is not None else Vector3D()
        self._shape = shape if shape is not None else Shape("undefined")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_direction(self):
        return self._direction

    def set_direction(self, direction_str: str):
        self._direction = Vector3D(direction_str)

    def get_position(self):
        return self._position

    def set_position(self, position_str: str):
        self._position = Vector3D(position_str)

    def get_shape(self):
        return self._shape

    def set_shape(self, shape):
        self._shape = shape

    def __repr__(self):
        return f"Body(name={self._name}, position={self._position}, shape={self._shape})"

    def print_info(self):
        print(f"\nBody Information:")
        print(f"Name: {self._name}")
        print(f"Position:")
        self._position.print_info()
        print(f"direction:")
        self._direction.print_info()
        print("Shape details:")
        self._shape.print_info()

    def _update_position(self, dt : float, bodies : [Body]):
        distances = [self._position.

    def _update_direction(self, dt : float, bodies : [Body]):
        pass

    def update(self, dt : float, bodies : [Body]):
        pass

