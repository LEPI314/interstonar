from Body import *
from Object.ShapeFactory import ShapeFactory
from Parsing import parse


def main():
    # Initialisation de la factory (Singleton)
    
    factory = ShapeFactory()
    
    data = parse("example.txt", factory)
    
    # Création de différentes bodies avec formes générées par la factory
    #bodies = [
    #    Body("Boule", position={"x": 1, "y": 2, "z": 3}, shape=factory.create_shape("circle")),
    #    Body("Boîte", position={"x": 0, "y": 0, "z": 0}, shape=factory.create_shape("box")),
    #    Body("Cylindre", position={"x": -1, "y": -1, "z": -1}, shape=factory.create_shape("cylinder")),
    #    Body("Torus", position={"x": 2, "y": 2, "z": 2}, shape=factory.create_shape("torus"))
    #]
    
    # Affichage des informations pour chaque body
    print("=== Liste des corps créés ===")
    for body in data:
        body.print_info()
        print("-" * 50)

if __name__ == "__main__":
    main()



#def main():
#    
#    SFactory = ShapeFactory()
#    data = parse("example.toml")