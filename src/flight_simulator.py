import numpy as np
from src.aircraft import Aircraft

class FlightSimulator:
    def __init__(self, aircraft: Aircraft, h0: float, v0: float, rho: float = 1.225):
        self.aircraft = aircraft
        self.h0 = h0  # Altitud inicial
        self.v0 = v0  # Velocidad inicial
        self.rho = rho  # Densidad del aire
        self.g = 9.81  # Gravedad

    def simulate(self, dt = 0.1):
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

        max_iter = 10000  # Para evitar bucles infinitos

        while h > 0 and max_iter > 0:
            # Calcular fuerzas
            L = 0.5 * self.rho * v**2 * S * CL
            D = 0.5 * self.rho * v**2 * S * CD

            # Evitar división por cero
            if L == 0:
                print("⚠️ Advertencia: Sustentación es cero. Se detiene la simulación.")
                break

            # Ángulo de planeo (simplificado)
            theta = np.arctan2(D, L)  # Más seguro que D / L

            # Componentes de velocidad
            vx = v * np.cos(theta)
            vy = -v * np.sin(theta)

            # Actualizar posición y tiempo
            x += vx * dt
            h += vy * dt
            t += dt

            # Actualizar velocidad por arrastre
            a_drag = D / m
            v -= a_drag * dt
            v = max(v, 0.1)  # evitar que se vuelva 0

            # Guardar valores
            alturas.append(h)
            distancias.append(x)
            velocidades.append(v)
            tiempos.append(t)

            max_iter -= 1

        if max_iter == 0:
            print("⚠️ Simulación detenida por exceso de iteraciones.")

        return{
            "alturas": alturas,
            "distancias": distancias,
            "velocidades": velocidades,
            "tiempos": tiempos
            }

