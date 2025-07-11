import numpy as np
from src.aircraft import Aircraft

class FlightSimulator:
    def __init__(self, aircraft: Aircraft, h0: float, v0: float, rho: float = 1.225):
        self.aircraft = aircraft
        self.h0 = h0  # Altitud inicial
        self.v0 = v0  # Velocidad inicial
        self.rho = rho  # Densidad del aire
        self.g = 9.81  # Gravedad

