from Body import Body
from Object.ShapeFactory import ShapeFactory


class Parser:
    _instance = None

    def __new__(cls):
        """Override __new__ pour contrôler la création d'instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_instance(cls):
        if cls._instance:
            return cls._instance
        cls.__new__()
        return cls._instance

    def parse(filePath):

        data: list[Body] = []

        with open(filePath, "r") as file:

            for lign in file:

                if lign.startswith("[[bodies]]"):
                    data.append(Body())

                if lign.startswith("type"):
                    print(lign.split('=', 1)[1].strip())
                    data[-1].set_shape(ShapeFactory.get_instance().create_shape(
                        lign.split('=', 1)[1].strip()))

                if lign.startswith("mass"):
                    data[-1].get_shape().set_mass(
                        lign.split('=', 1)[1].strip())

                if lign.startswith("radius"):
                    data[-1].get_shape().set_radius(lign.split('=', 1)[1].strip())

                if lign.startswith("position"):
                    data[-1].set_position(lign.split('=', 1)[1].strip())

                if lign.startswith("direction"):
                    data[-1].set_direction(lign.split('=', 1)[1].strip())

                if lign.startswith("sides"):
                    data[-1].get_shape().set_sides(lign.split('=', 1)[1].strip())

                if lign.startswith("inner_radius"):
                    data[-1].get_shape().set_inner_radius(
                        lign.split('=', 1)[1].strip())

                if lign.startswith("outer_radius"):
                    data[-1].get_shape().set_outer_radius(
                        lign.split('=', 1)[1].strip())

                if lign.startswith("height"):
                    data[-1].get_shape().set_height(
                        lign.split('=', 1)[1].strip().split("#", 1)[0].strip())

                if lign.startswith("radius"):
                    data[-1].get_shape().set_radius(lign.split('=', 1)[1].strip())

        return data
