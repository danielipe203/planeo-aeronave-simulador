import numpy as np
from src.aircraft import Aircraft

class FlightSimulator:
    def __init__(self, aircraft: Aircraft, h0: float, v0: float, rho: float = 1.225):
        self.aircraft = aircraft
        self.h0 = h0  # Altitud inicial
        self.v0 = v0  # Velocidad inicial
        self.rho = rho  # Densidad del aire
        self.g = 9.81  # Gravedad

    def simulate(self, dt=0.1):
        # Inicializar condiciones
        h = self.h0
        v = self.v0
        x = 0
        t = 0

        m = self.aircraft.mass
        S = self.aircraft.wing_area
        CL = self.aircraft.cl
        CD = self.aircraft.cd

        # Guardar resultados
        alturas = [h]
        distancias = [x]
        velocidades = [v]
        tiempos = [t]

        # Bucle de simulación
        while h > 0:
            # Calcular fuerzas
            L = 0.5 * self.rho * v**2 * S * CL
            D = 0.5 * self.rho * v**2 * S * CD

            # Ángulo de planeo (simplificado)
            theta = np.arctan(D / L)

            # Componentes de velocidad
            vx = v * np.cos(theta)
            vy = -v * np.sin(theta)

            # Actualizar posición y tiempo
            x += vx * dt
            h += vy * dt
            t += dt

            # Actualizar velocidad (resistencia)
            a_drag = D / m
            v -= a_drag * dt
            if v < 0:
                v = 0.1  # Para evitar que se detenga

            # Guardar valores
            alturas.append(h)
            distancias.append(x)
            velocidades.append(v)
            tiempos.append(t)

        # Retornar los resultados
        return {
            "alturas": alturas,
            "distancias": distancias,
            "velocidades": velocidades,
            "tiempos": tiempos
        }
