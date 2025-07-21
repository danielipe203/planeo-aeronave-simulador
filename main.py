from src.aircraft import Aircraft
from src.flight_simulator import FlightSimulator
from src.plotter import Plotter

def main():
    # Crear el avión con parámetros definidos
    avion = Aircraft(
        mass=800,           # kg
        wing_area=16.2,     # m²
        cl=1.2,             # Coef. sustentación
        cd=0.08             # Coef. arrastre
    )

    # Crear simulador de planeo
    simulador = FlightSimulator(
        aircraft=avion,
        h0=3000,    # Altura inicial (m)
        v0=60       # Velocidad inicial (m/s)
    )

    # Ejecutar la simulación
    resultado = simulador.simulate()

    # Imprimir resultados por consola
    print("\n--- RESULTADOS ---")
    print("Altura inicial:", resultado['alturas'][0], "m")
    print("Distancia recorrida:", round(resultado['distancias'][-1], 2), "m")
    print("Tiempo total:", round(resultado['tiempos'][-1], 2), "s")
    print("Velocidad final:", round(resultado['velocidades'][-1], 2), "m/s")

    # Mostrar gráficas
    plotter = Plotter()
    plotter.plot_trajectory(resultado["distancias"], resultado["alturas"])
    plotter.plot_velocity(resultado["tiempos"], resultado["velocidades"])

if __name__ == "__main__":
    main()

