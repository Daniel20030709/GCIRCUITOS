import math

class Calculator:
    def __init__(self):
        pass

    def calcular_atenuacion(self, potencia_entrada, potencia_salida):
        atenuacion = 10 * math.log10(potencia_salida / potencia_entrada)
        return atenuacion

    def calcular_factor_potencia(self, potencia_activa, potencia_aparente):
        factor_potencia = potencia_activa / potencia_aparente
        return factor_potencia

    def frecuencia(self, R, C):
        return 1 / (2 * math.pi * R * C)

    def impedancia_rlc(self, R, L, C, f):
        omega = 2 * math.pi * f
        Z_R = R
        Z_L = 1j * omega * L
        Z_C = -1j / (omega * C)
        Z = Z_R + Z_L + Z_C
        return Z

    def calcular_potencia_activa(self, voltaje, corriente, factor_potencia):
        potencia_activa = voltaje * corriente * factor_potencia
        return potencia_activa

    def calcular_potencia_aparente(self, voltaje, corriente):
        potencia_aparente = voltaje * corriente
        return potencia_aparente

    def calcular_potencia_electrica(self, voltaje, corriente):
        potencia_electrica = voltaje * corriente
        return potencia_electrica

    def calcular_potencia_reactiva(self, potencia_activa, potencia_aparente):
        potencia_reactiva = (potencia_aparente**2 - potencia_activa**2)**0.5
        return potencia_reactiva

    def calcular_tension_electrica(self, resistencia, corriente):
        tension_electrica = corriente * resistencia
        return tension_electrica

    def calcular_frecuencia_compleja(self, L, C, R):
        frecuencia_compleja = (1 / (2 * math.pi)) * ((1 / (L * C)) - (R / (2 * L)))
        return frecuencia_compleja

    def calcular_longitud_onda(self, frecuencia):
        velocidad_luz = 299792458 # m/s
        longitud_onda = velocidad_luz / frecuencia
        return longitud_onda

    def calcular_potencia_energia(self, tiempo, potencia):
        energia = potencia * tiempo
        return energia

    def calcular_trabajo(self, fuerza, distancia):
        trabajo = fuerza * distancia
        return trabajo

    def calcular_velocidad_angular(self, frecuencia):
        velocidad_angular = 2 * math.pi * frecuencia
        return velocidad_angular

    def calcular_periodo(self, frecuencia):
        periodo = 1 / frecuencia
        return periodo

    def solicitar_opcion(self):
     while True:
        print("Seleccione una opción:")
        print("1. Calcular atenuación")
        print("2. Calcular factor de potencia")
        print("3. Calcular frecuencia")
        print("4. Calcular impedancia RLC")
        print("5. Calcular potencia activa")
        print("6. Calcular potencia aparente")
        print("7. Calcular potencia electrica")
        print("8. Calcular potencia reactiva")
        print("9. Calcular tension electrica")
        print("10. Calcular frecuencia compleja")
        print("11. Calcular longitud de onda")
        print("12. Calcular potencia energia")
        print("13. Calcular trabajo")
        print("14. Calcular velocidad angular")
        print("15. Calcular periodo")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            potencia_entrada = float(input("Ingrese la potencia de entrada: "))
            potencia_salida = float(input("Ingrese la potencia de salida: "))
            resultado = self.calcular_atenuacion(potencia_entrada, potencia_salida)
            print("La atenuación es: ", resultado)
        elif opcion == "2":
            potencia_activa = float(input("Ingrese la potencia activa: "))
            potencia_aparente = float(input("Ingrese la potencia aparente: "))
            resultado = self.calcular_factor_potencia(potencia_activa, potencia_aparente)
            print("El factor de potencia es: ", resultado)

        elif opcion == "3":
            frecuencia = float(input("Ingrese la frecuencia: "))
            resultado = self.calcular_frecuencia(frecuencia)
            print("La frecuencia es: ", resultado)
        elif opcion == "4":
            R = float(input("Ingrese la resistencia: "))
            L = float(input("Ingrese la inductancia: "))
            C = float(input("Ingrese la capacitancia: "))
            f = float(input("Ingrese la frecuencia: "))
            Z = self.impedancia_rlc(R, L, C, f)
            print("La impedancia es:", Z)

        elif opcion == "5":
            voltaje = float(input("Ingrese el valor del voltaje: "))
            corriente = float(input("Ingrese el valor de la corriente: "))
            factor_potencia = float(input("Ingrese el valor del factor de potencia: "))
            potencia_activa = self.calcular_potencia_activa(voltaje, corriente, factor_potencia)
            print("La potencia activa es:", potencia_activa)
        elif opcion == "6":
            voltaje = float(input("Ingrese el valor del voltaje: "))
            corriente = float(input("Ingrese el valor de la corriente: "))
            potencia_aparente = self.calcular_potencia_aparente(voltaje, corriente)
            print("La potencia aparente es:", potencia_aparente)
        elif opcion == "7":
            voltaje = float(input("Ingrese el valor del voltaje: "))
            corriente = float(input("Ingrese el valor de la corriente: "))
            potencia_electrica = self.calcular_potencia_electrica(voltaje, corriente)
            print("La potencia electrica es:", potencia_electrica)
        elif opcion == "8":
            potencia_activa = float(input("Ingrese el valor de la potencia activa: "))
            potencia_aparente = float(input("Ingrese el valor de la potencia aparente: "))
            potencia_reactiva = self.calcular_potencia_reactiva(potencia_activa, potencia_aparente)
            print("La potencia reactiva es:", potencia_reactiva)
        elif opcion == "9":
            resistencia = float(input("Ingrese el valor de la resistencia: "))
            corriente = float(input("Ingrese el valor de la corriente: "))
            tension_electrica = self.calcular_tension_electrica(resistencia, corriente)
            print("La tension electrica es:", tension_electrica)

        elif opcion == "10":
            L = float(input("Ingrese el valor de L: "))
            C = float(input("Ingrese el valor de C: "))
            R = float(input("Ingrese el valor de R: "))
            frecuencia_comp = self.calcular_frecuencia_compleja(L, C, R)
            print("La frecuencia compleja es:", frecuencia_comp)
        elif opcion == "11":
            frecuencia = float(input("Ingrese el valor de la frecuencia: "))
            longitud_onda = self.calcular_longitud_onda(frecuencia)
            print("La longitud de onda es:", longitud_onda)
        elif opcion == "12":
            tiempo = float(input("Ingrese el valor del tiempo: "))
            potencia = float(input("Ingrese el valor de la potencia: "))
            energia = self.calcular_potencia_energia(tiempo, potencia)
            print("La energia es:", energia)
        elif opcion == "13":
            fuerza = float(input("Ingrese el valor de la fuerza: "))
            distancia = float(input("Ingrese el valor de la distancia: "))
            trabajo = self.calcular_trabajo(fuerza, distancia)
            print("El trabajo es:", trabajo)
        elif opcion == "14":
            frecuencia = float(input("Ingrese el valor de la frecuencia: "))
            velocidad_angular = self.calcular_velocidad_angular(frecuencia)
            print("La velocidad angular es:", velocidad_angular)
        elif opcion == "15":
            frecuencia = float(input("Ingrese el valor de la frecuencia: "))
            periodo = self.calcular_periodo(frecuencia)
            print("El periodo es:", periodo)
        choice = input("¿Desea continuar? (s/n): ")
        if choice.lower() != 's':
            break
            
        
            
calc = Calculator()
calc.solicitar_opcion()

