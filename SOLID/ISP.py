from abc import ABC, abstractmethod

# Creamos una clase abstracta Trabajador
class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

# Creamos una clase abstracta Comer
class Comer(ABC):

    @abstractmethod
    def comer(self):
        pass

# Creamos una clase abstracta Durmiendo
class Durmiendo(ABC):

    @abstractmethod
    def dormir(self):
        pass

# Creamos una clase Humano que hereda de Trabajador, Durmiendo y Comer
class Humano(Trabajador, Durmiendo, Comer):

    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")

# Creamos una clase Robot que hereda de Trabajador
class Robot(Trabajador):

    def trabajar(self):
        print("El robot está trabajando")

# Creamos una instancia de Robot y Humano
robot = Robot()
humano = Humano()

# Llamamos al método trabajar() de cada instancia
robot.trabajar()  # Salida: El robot está trabajando
humano.trabajar()  # Salida: El humano está trabajando
