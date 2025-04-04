from .shape import Shape


class Sphere(Shape):
    def __init__(self, radius: float = 1.0):
        super().__init__("sphere")
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def print_info(self):
        super().print_info()
        print(f"Radius: {self._radius}")
