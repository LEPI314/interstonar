import re
import math


class Vector3D:
    def __init__(self, value=None):
        if value is None:
            self.x, self.y, self.z = (0, 0, 0)

        elif isinstance(value, str):
            self._from_string(value)

        elif isinstance(value, dict):
            self._from_dict(value)
        else:
            raise TypeError(
                "Vector3D constructor only accepts" +
                "a string like '{x = 1, y = 2, z = 3}'")

    def _from_string(self, string: str):
        cleaned = string.split("#", 1)[0].strip()
        self.x = self._extract_value(cleaned, "x")
        self.y = self._extract_value(cleaned, "y")
        self.z = self._extract_value(cleaned, "z")

    def _from_dict(self, dico: dict):
        self.x = dico.x
        self.y = dico.y
        self.z = dico.z

    def _extract_value(self, string: str, axis: str) -> float:
        match = re.search(rf'{axis}\s*=\s*(-?\d+(?:\.\d+)?)', string)
        return float(match.group(1)) if match else 0.0

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            return NotImplemented
        return Vector3D({
            'x': {self.x + other.x},
            'y': {self.y + other.y},
            'z': {self.z + other.z}
        })

    def __sub__(self, other):
        if not isinstance(other, Vector3D):
            return NotImplemented
        return Vector3D({
            'x': {self.x - other.x},
            'y': {self.y - other.y},
            'z': {self.z - other.z}
        })

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")

        return Vector3D({
            'x': {self.x / scalar},
            'y': {self.y / scalar},
            'z': {self.z / scalar}
        })

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector3D({
            'x': {self.x * scalar},
            'y': {self.y * scalar},
            'z': {self.z * scalar}
        })

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dst(self, other):
        return self.norm(self - other)

    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"

    def print_info(self):
        print(f"{{'x': {self.x}, 'y': {self.y}, 'z': {self.z}}}")
