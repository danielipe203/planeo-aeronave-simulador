import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self, resultados):
        self.resultados = resultados

    def plot_all(self):
        tiempos = self.resultados["tiempos"]
        alturas = self.resultados["alturas"]
        distancias = self.resultados["distancias"]
        velocidades = self.resultados["velocidades"]

        # Asegurar que la carpeta exista
        os.makedirs("graficas", exist_ok=True)

        # Altura vs Tiempo
        plt.figure()
        plt.plot(tiempos, alturas)
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Altura (m)")
        plt.title("Altura vs Tiempo")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("graficas/altura_vs_tiempo.png")

        # Distancia vs Tiempo
        plt.figure()
        plt.plot(tiempos, distancias)
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Distancia (m)")
        plt.title("Distancia vs Tiempo")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("graficas/distancia_vs_tiempo.png")

        # Velocidad vs Tiempo
        plt.figure()
        plt.plot(tiempos, velocidades)
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Velocidad (m/s)")
        plt.title("Velocidad vs Tiempo")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("graficas/velocidad_vs_tiempo.png")
