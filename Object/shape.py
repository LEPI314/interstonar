
class Shape:
    def __init__(self, shape_type: str, mass: int = 0):
        self.shape_type = shape_type
        self.mass = mass

    def __str__(self):
        return self.shape_type

    def set_mass(self, mass):
        self.mass = mass

    def get_mass(self):
        return self.mass

    def print_info(self):
        print(f"Shape type: {self.shape_type}")
        print(f"mass = {self.mass}")