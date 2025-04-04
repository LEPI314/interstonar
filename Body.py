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
    
    def set_direction(self, direction):
        self.direction = direction

    def get_position(self):
        return self._position

    def set_position(self, x, y, z):
        self._position = {"x": x, "y": y, "z": z}

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