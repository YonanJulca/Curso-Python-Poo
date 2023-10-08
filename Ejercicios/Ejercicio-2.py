class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base (Persona)
        self.grado = grado
    
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

# Creamos una instancia de Estudiante
estudiante = Estudiante("Yonan", "21", "5")

# Llamamos al método mostrar_datos de la clase Persona
estudiante.mostrar_datos()

# Llamamos al método mostrar_grado de la clase Estudiante
estudiante.mostrar_grado()
