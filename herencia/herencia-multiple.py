class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        return super().mostrar_habilidad()  # Debes retornar el resultado en lugar de imprimirlo

# Creamos una instancia de EmpleadoArtista
roberto = EmpleadoArtista("Yonan", 21, "Peru", "cantar", 1200, "mirco")

# Llamamos al método presentarse y mostramos la habilidad del artista
roberto.presentarse()  # Esto imprimirá "Mi habilidad es: cantar"
