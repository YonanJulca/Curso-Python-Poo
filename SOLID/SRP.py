class TanqueCombustible:
    def __init__(self):
        self.combustible = 100  # Inicializamos el tanque con 100 unidades de combustible

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad  # Añadimos la cantidad de combustible especificada

    def obtener_combustible(self):
        return self.combustible  # Devolvemos la cantidad de combustible actual

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad  # Usamos la cantidad de combustible especificada


class Auto():
    def __init__(self, tanque):
        self.posicion = 0  # Inicializamos la posición del auto en 0
        self.tanque = tanque  # Asignamos el tanque de combustible al auto

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            # Si hay suficiente combustible para mover la distancia especificada
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)  # Usamos la mitad de la distancia en combustible
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")  # Si no hay suficiente combustible

    def obtener_posicion(self):
        return self.posicion  # Devolvemos la posición actual del auto


# Creamos una instancia de TanqueCombustible
tanque = TanqueCombustible()

# Creamos una instancia de Auto y le asignamos el tanque de combustible
autito = Auto(tanque)

# Imprimimos la posición inicial del auto
print(autito.obtener_posicion())

# Movemos el auto y verificamos la nueva posición
autito.mover(10)
print(autito.obtener_posicion())

autito.mover(20)
print(autito.obtener_posicion())

autito.mover(60)
print(autito.obtener_posicion())

autito.mover(100)
print(autito.obtener_posicion())

autito.mover(120)
