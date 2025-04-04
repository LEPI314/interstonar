import math


class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            return NotImplemented
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector3D):
            return NotImplemented
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"
