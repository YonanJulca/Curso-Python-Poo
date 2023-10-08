from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    # Método abstracto que debe ser implementado por las subclases.
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")
        # Método que imprime una presentación básica de la persona.

class Estudiante(Persona):
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        # Implementación del método abstracto para un estudiante.
        
class Trabajador(Persona):
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")
        # Implementación del método abstracto para un trabajador.
        

# Ejemplos de uso:

# Crear una instancia de Estudiante
yonan = Estudiante("Yonan", 21, "Masculino", "programación")

# Llamar al método específico para un estudiante
yonan.hacer_actividad()  
# Esto imprimirá "Estoy estudiando: programación"

# Llamar a un método común para todas las personas
yonan.presentarse()  
# Esto imprimirá "Hola, me llamo Yonan y tengo 21 años"


# Crear una instancia de Trabajador
juan = Trabajador("Juan", 28, "Masculino", "programación")

# Llamar al método específico para un trabajador
juan.hacer_actividad()  
# Esto imprimirá "Actualmente estoy trabajando en el rubro de: programación"
