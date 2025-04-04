from SolarSystem import SolarSystem


def main():
    # Initialisation du système solaire
    system = SolarSystem(filepath="example.txt")

    # Création de différentes bodies avec formes générées par la factory
    # bodies = [
    #    Body("Boule", position={"x": 1, "y": 2, "z": 3}, shape=factory.create_shape("circle")),
    #    Body("Boîte", position={"x": 0, "y": 0, "z": 0}, shape=factory.create_shape("box")),
    #    Body("Cylindre", position={"x": -1, "y": -1, "z": -1}, shape=factory.create_shape("cylinder")),
    #    Body("Torus", position={"x": 2, "y": 2, "z": 2}, shape=factory.create_shape("torus"))
    # ]

    # Affichage des informations pour chaque body
    system.print_info()


if __name__ == "__main__":
    main()
