from .shape import Shape

class Box(Shape):
    def __init__(self, x: float = 10.0, y: float = 10.0, z: float = 10.0):
        super().__init__("box")
        self._sides = {"x": x, "y": y, "z": z}

    def get_sides(self):
        return self._sides

    def set_sides(self, x, y, z):
        self._sides = {"x": x, "y": y, "z": z}

    def print_info(self):
        super().print_info()
        print(f"Sides (x,y,z): {self._sides['x']}, {self._sides['y']}, {self._sides['z']}")