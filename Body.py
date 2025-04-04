import re
from Object.shape import Shape


class Body:

    def __init__(self, name: str = "Unnamed", position: dict = None, direction: dict = None, shape: Shape = None):
        self._name = name
        self._position = position if position is not None else {"x": 0, "y": 0, "z": 0}
        self._direction = direction if direction is not None else {"x": 0, "y": 0, "z": 0}
        self._shape = shape if shape is not None else Shape("undefined")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_direction(self):
        return self._direction

    def set_direction(self, direction_str: str):
        self._direction = self._parse_vector_string(direction_str)

    def get_position(self):
        return self._position

    def set_position(self, position_str: str):
        self._position = self._parse_vector_string(position_str)

    def get_shape(self):
        return self._shape

    def set_shape(self, shape):
        self._shape = shape

    def __repr__(self):
        return f"Body(name={self._name}, position={self._position}, shape={self._shape})"

    def print_info(self):
        print(f"\nBody Information:")
        print(f"Name: {self._name}")
        print(f"Position: x={self._position['x']}, y={self._position['y']}, z={self._position['z']}")
        print("Shape details:")
        self._shape.print_info()

    def _parse_vector_string(self, vector_str: str) -> dict:
        """
        Parse a string of the form "{x = 10, y = 20, z = 30}" and return a dict like {'x': 10, 'y': 20, 'z': 30}
        """
        vector = {"x": 0, "y": 0, "z": 0}
        matches = re.findall(r'([xyz])\s*=\s*(-?\d+(?:\.\d+)?)', vector_str)
        for axis, value in matches:
            vector[axis] = float(value) if '.' in value else int(value)
        return vector
