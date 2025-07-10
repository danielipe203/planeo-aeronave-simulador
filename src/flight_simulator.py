import numpy as np
from src.aircraft import aircraft

class FlightSimulator:
    def_init_(self, aircraft: Aircraft, h0: float, v0:float, rho: float: 1.225):
        self.aircraft = aircraft #altitud inicial
        self.h0 = h0 #velocidad inicial 
        self.rho = rho #densidad del aire
        self.g = 9.81 #gravedad

def simulate(self, dt=0.1):
    #inicializar condiciones
    h =slef.h0
    v = self.v0
    x = 0
    y = 0

    m = self.aircraft.mass
    S = self.aircraft.wing_area
    CL =self.aircraft.cl
    CD = self.aircraft.cd

    #guardar resultados
    alturas = [h]
    distancias = [x]
    velocidades = [v]
    tiempos = [t]

    while h > 0:
        L = 0.5*self.rho * v**2 * S * CL
