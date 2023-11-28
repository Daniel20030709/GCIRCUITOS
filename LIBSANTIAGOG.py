import math

class AttenuationCalculator:
    def __init__(self, potencia_entrada, potencia_salida):
        self.potencia_entrada = potencia_entrada
        self.potencia_salida = potencia_salida

    def calcular_atenuacion(self):
        atenuacion = 10 * math.log10(self.potencia_salida / self.potencia_entrada)
        return atenuacion

class FactorPotencia:
    def __init__(self, potencia_activa, potencia_aparente):
        self.potencia_activa = potencia_activa
        self.potencia_aparente = potencia_aparente

    def calcular_factor_potencia(self):
        factor_potencia = self.potencia_activa / self.potencia_aparente
        return factor_potencia

class RCFilterfrecuencia:
    def __init__(self, R, C):
        self.R = R
        self.C = C

    def cutoff_frequency(self):
        """
        Calcula la frecuencia de corte de un circuito RC en serie.

        Retorna:
        float: Frecuencia de corte en hertzios.
        """
        return 1 / (2 * math.pi * self.R * self.C)

class RLCFilter:
    def __init__(self, R, L, C):
        self.R = R
        self.L = L
        self.C = C

    def impedance_rlc_series(self, f):
        """
        Calcula la impedancia de un circuito RLC en serie.

        Parámetros:
        f (float): Frecuencia en hertzios.

        Retorna:
        float: Impedancia en ohmios.
        """
        omega = 2 * math.pi * f
        Z_R = self.R
        Z_L = 1j * omega * self.L
        Z_C = -1j / (omega * self.C)
        Z = Z_R + Z_L + Z_C
        return abs(Z)

class PotenciaActiva:
    def __init__(self, voltaje, corriente, factor_potencia):
        self.voltaje = voltaje
        self.corriente = corriente
        self.factor_potencia = factor_potencia

    def calcular_potencia_activa(self):
        potencia_activa = self.voltaje * self.corriente * self.factor_potencia
        return potencia_activa

class PotenciaAparente:
    def __init__(self, voltaje, corriente):
        self.voltaje = voltaje
        self.corriente = corriente

    def calcular_potencia_aparente(self):
        potencia_aparente = self.voltaje * self.corriente
        return potencia_aparente

class PotenciaElectrica:
    def __init__(self, voltaje, corriente):
        self.voltaje = voltaje
        self.corriente = corriente

    def calcular_potencia_electrica(self):
        potencia_electrica = self.voltaje * self.corriente
        return potencia_electrica

class PotenciaReactiva:
    def __init__(self, potencia_activa, potencia_aparente):
        self.potencia_activa = potencia_activa
        self.potencia_aparente = potencia_aparente

    def calcular_potencia_reactiva(self):
        potencia_reactiva = (self.potencia_aparente**2 - self.potencia_activa**2)**0.5
        return potencia_reactiva

class TensionElectrica:
    def __init__(self, resistencia, corriente):
        self.resistencia = resistencia
        self.corriente = corriente

    def calcular_tension_electrica(self):
        tension_electrica = self.corriente * self.resistencia
        return tension_electrica
