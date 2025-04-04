from Body import Body
from Object.ShapeFactory import ShapeFactory


class Parser:
    _instance = None
    _data = []

    def __new__(cls):
        """Override __new__ pour contrôler la création d'instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        cls.__new__(cls)
        return cls._instance

    def error_handling(cls, function: None, args):
        try:
            function(cls, args)
        except:
            print("Parse Error")
            exit(84)

    def parse(cls, filePath):
        with open(filePath, "r") as file:
            for lign in file:
                if lign.startswith("[[bodies]]"):
                    cls._data.append(Body())

                # Appel des méthodes associées avec error_handling
                if lign.startswith("type"):
                    cls.error_handling(
                        cls.handle_type, lign)

                elif lign.startswith("mass"):
                    cls.error_handling(
                        cls.handle_mass, lign)

                elif lign.startswith("radius"):
                    cls.error_handling(
                        cls.handle_radius, lign)

                elif lign.startswith("position"):
                    cls.error_handling(
                        cls.handle_position, lign)

                elif lign.startswith("direction"):
                    cls.error_handling(
                        cls.handle_direction, lign)

                elif lign.startswith("sides"):
                    cls.error_handling(
                        cls.handle_sides, lign)

                elif lign.startswith("inner_radius"):
                    cls.error_handling(
                        cls.handle_inner_radius, lign)

                elif lign.startswith("outer_radius"):
                    cls.error_handling(
                        cls.handle_outer_radius, lign)

                elif lign.startswith("height"):
                    cls.error_handling(
                        cls.handle_height, lign)

        return cls._data

    def _lign_to_data(cls, lign: str):
        return lign.split('=', 1)[1].strip()

    # Méthodes pour chaque type de ligne
    def handle_type(cls, function: None, lign: str):
        print(cls._lign_to_data(lign))
        cls._data[-1].set_shape(ShapeFactory.get_instance().create_shape(
            cls._lign_to_data(lign)))

    def handle_mass(cls, function, lign: str):
        cls._data[-1].get_shape().set_mass(cls._lign_to_data(lign))

    def handle_radius(cls, function, lign: str):
        cls._data[-1].get_shape().set_radius(cls._lign_to_data(lign))

    def handle_position(cls, function, lign: str):
        cls._data[-1].set_position(cls._lign_to_data(lign))

    def handle_direction(cls, function, lign: str):
        cls._data[-1].set_direction(cls._lign_to_data(lign))

    def handle_sides(cls, function, lign: str):
        cls._data[-1].get_shape().set_sides(cls._lign_to_data(lign))

    def handle_inner_radius(cls, function, lign: str):
        cls._data[-1].get_shape().set_inner_radius(cls._lign_to_data(lign))

    def handle_outer_radius(cls, function, lign: str):
        cls._data[-1].get_shape().set_outer_radius(cls._lign_to_data(lign))

    def handle_height(cls, function, lign: str):
        cls._data[-1].get_shape().set_height(
                cls._lign_to_data(lign).split("#", 1)[0].strip())
