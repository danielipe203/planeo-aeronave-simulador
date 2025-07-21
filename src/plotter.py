import matplotlib.pyplot as plt
class Plotter:
    def __init__(self):
        pass
    def plot_trajectory(self, distancias, alturas):
        """Gráfica de la trayectoria (altura vs distancia)"""
        plt.figure(figsize=(10,5))
        plt.plot(distancias, alturas, color='blue', label='Trayectoria de Planeo')
        plt.xlabel("Distancia horizontal (m)")
        plt.ylabel("Altura (m)")
        plt.title("Simulación de Trayectoria de Planeo")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    def plot_velocity(self, tiempos, velocidades):
        """Gráfica de velocidad vs tiempo"""
        plt.figure(figsize=(10, 5))
        plt.plot(tiempos, velocidades, color='green', label='Velocidad')
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Velocidad (m/s)")
        plt.title("Velocidad vs Tiempo durante el Planeo")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()