from Object.ShapeFactory import ShapeFactory
from Parsing import parse


class SolarSystem:
    def __init__(self, filepath, dt=60*60):
        factory = ShapeFactory()
        self._data = parse(filepath, factory)
        self._dt = dt

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def print_info(self):
        print("=== Liste des corps créés ===")
        for body in self._data:
            body.print_info()
            print("-" * 50)

    def update(self):
        for body in self._data:
            body.update(self._dt)

        for body in self._data:
            body.finalise_update()

        for body in self._data:
            for other in filter((lambda x: x != body), self._data):
                if body.collide(other):
                    pass
