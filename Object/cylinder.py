from .shape import Shape

class Cylinder(Shape):

    def __init__(self, radius: float = 1.0, height: float = None):
        super().__init__("cylinder")
        self._radius = radius
        self._height = height

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height
    
    def print_info(self):
        super().print_info()
        print(f"Radius: {self._radius}")
        print(f"Height: {self._height}")