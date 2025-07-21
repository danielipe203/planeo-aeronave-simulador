# ✈️ Simulador de Planeo de Aeronave sin Motor

Este proyecto simula el planeo de una aeronave sin motor a partir de condiciones iniciales, permitiendo estimar la trayectoria, distancia recorrida, tiempo de planeo y velocidad final. La visualización incluye gráficas de comportamiento clave de la simulación.

---

## 👨‍💻 Integrantes del equipo

- **Daniel Felipe Segura** – Simulación de vuelo (`flight_simulator.py`)
- **Alejandra Zapata** – Modelo físico del avión (`aircraft.py`)
- **Juanita Arenas** – Visualización de resultados (`plotter.py`)

---

## 🎯 Objetivo del proyecto

Diseñar un simulador que permita modelar el comportamiento de una aeronave sin propulsión tras una falla, estimando su capacidad de planeo y apoyando decisiones para un aterrizaje seguro.

---

## 🧮 Parámetros de entrada

El sistema recibe:

- Altitud inicial (`h0`)
- Velocidad inicial (`v0`)
- Masa del avión (`mass`)
- Área alar (`wing_area`)
- Coeficiente de sustentación (`CL`)
- Coeficiente de arrastre (`CD`)
- Densidad del aire (`rho`)

---

## 🧠 ¿Qué simula?

- La evolución de la altura, velocidad y posición horizontal en función del tiempo.
- Las fuerzas de sustentación y arrastre.
- El ángulo de planeo.
- Una estimación del tiempo y distancia hasta el aterrizaje.

---

## 📊 Visualización de resultados

El sistema genera automáticamente tres gráficas al finalizar la simulación:

- Altura vs Tiempo
- Distancia vs Tiempo
- Velocidad vs Tiempo

Estas se guardan en la carpeta `/graficas` como archivos `.png`.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- `numpy`
- `matplotlib`
- `os` y `math`

---

## ▶️ Ejecución del simulador

1. Clona el repositorio:
   ```bash
   git clone https://github.com/danielipe203/planeo-aeronave-simulador.git
   cd planeo-aeronave-simulador
