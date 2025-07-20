class Aircraft:
    def __init__(self, mass, wing_area, cl, cd):
        """
        Inicializa una nueva aeronave con sus propiedades aerodinámicas.

        Parámetros:
        - mass: masa del avión (kg)
        - wing_area: área alar (m^2)
        - cl: coeficiente de sustentación
        - cd: coeficiente de arrastre
        """
        self.mass = mass
        self.wing_area = wing_area
        self.cl = cl
        self.cd = cd

    def __str__(self):
        return f"Aeronave (masa={self.mass} kg, área={self.wing_area} m², CL={self.cl}, CD={self.cd})"


