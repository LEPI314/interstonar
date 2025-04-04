import re
from .shape import Shape

class Box(Shape):
    def __init__(self, x: float = 10.0, y: float = 10.0, z: float = 10.0):
        super().__init__("box")
        self._sides = {"x": x, "y": y, "z": z}

    def get_sides(self):
        return self._sides

    def set_sides(self, str):
        self._sides = self._parse_vector_string(str)

    def print_info(self):
        super().print_info()
        print(f"Sides (x,y,z): {self._sides['x']}, {self._sides['y']}, {self._sides['z']}")
        
    def _parse_vector_string(self, vector_str: str) -> dict:
        """
        Parse a string of the form "{x = 10, y = 20, z = 30}" and return a dict like {'x': 10, 'y': 20, 'z': 30}
        """
        vector = {"x": 0, "y": 0, "z": 0}
        matches = re.findall(r'([xyz])\s*=\s*(-?\d+(?:\.\d+)?)', vector_str)
        for axis, value in matches:
            vector[axis] = float(value) if '.' in value else int(value)
        return vector