from src.aircraft import Aircraft
from src.flight_simulator import FlightSimulator
from src.plotter import Plotter

if __name__ == "__main__":
    # Crear instancia del avión
    avion = Aircraft(mass=800, wing_area=16.2, cl=1.2, cd=0.08)

    # Crear simulador con condiciones iniciales
    sim = FlightSimulator(aircraft=avion, h0=3000, v0=60)

    # Ejecutar simulación
    resultado = sim.simulate()

    # Mostrar algunos resultados por consola
    print("Alturas (primeros 10 valores):", resultado["alturas"][:10])
    print("Distancia final:", resultado["distancias"][-1])
    print("Tiempo total de planeo:", resultado["tiempos"][-1])

    # Graficar la trayectoria
    plotter = Plotter()
    plotter.plot_trajectory(resultado["distancias"], resultado["alturas"])

