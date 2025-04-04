from Parsing import Parser


class SolarSystem:
    def __init__(self, filepath, mode='g', dt=60*60):
        # TODO : Global / Local mode (argv)
        self._data = Parser.get_instance().parse(filepath)
        self._dt = dt
        self._mode = mode

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

        # TODO : Collision detection
