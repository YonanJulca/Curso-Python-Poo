class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    # El método __str__ define cómo se debe imprimir una instancia de la clase Persona.

    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    # El método __repr__ define cómo se debe representar una instancia de la clase Persona en su forma "oficial".

    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
    # El método __add__ sobrecarga el operador de adición (+) para la clase Persona.
    # En este caso, crea una nueva instancia de Persona cuya edad es la suma de las edades de las dos personas
    # y cuyo nombre es la concatenación de los nombres de las dos personas.

# Creamos instancias de Persona
yonan = Persona("Yonan", 21)
sergio = Persona("Sergio", 24)

# Sumamos las edades de yonan y sergio para crear una nueva persona
nueva_persona = yonan + sergio

# Imprimimos la edad de la nueva persona
print(nueva_persona.edad)  # Esto imprimirá 45, que es la suma de 21 y 24
