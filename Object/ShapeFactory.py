from .cylinder import Cylinder
from .Box import Box
from .sphere import Sphere
from .torus import Torus

class ShapeFactory:
    
    _instance = None
    
    _shape_classes = {
        "\"sphere\"": Sphere,
        "\"box\"": Box,
        "\"cylinder\"": Cylinder,
        "\"torus\"": Torus
    }

    def __new__(cls):
        """Override __new__ pour contrôler la création d'instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def create_shape(cls, shape_type: str):
        """Crée un objet en fonction du type donné."""
        shape_class = cls._shape_classes.get(shape_type.lower())
        if shape_class:
            return shape_class()
        else:
            return None