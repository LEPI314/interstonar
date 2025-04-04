from .shape import Shape

class Torus(Shape):
    def __init__(self, inner_radius: float = 3.0, outer_radius: float = 1.0):
        super().__init__("torus")
        self._inner_radius = inner_radius
        self._outer_radius = outer_radius

    def get_inner_radius(self):
        return self._inner_radius

    def set_inner_radius(self, inner_radius):
        self._inner_radius = inner_radius

    def get_outer_radius(self):
        return self._outer_radius

    def set_outer_radius(self, outer_radius):
        self._outer_radius = outer_radius
    
    def print_info(self):
        super().print_info()
        print(f"Inner radius: {self._inner_radius}")
        print(f"Outer radius: {self._outer_radius}")