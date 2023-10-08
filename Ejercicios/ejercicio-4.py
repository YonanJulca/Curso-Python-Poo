class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    # El método __repr__ define cómo se debe representar una instancia de la clase en su forma "oficial".

    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 1.5)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 1.2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    # El método __add__ sobrecarga el operador de adición (+) para la clase Personaje.
    # En este caso, crea un nuevo personaje cuya fuerza es la media geométrica de las fuerzas
    # y cuya velocidad es la media geométrica de las velocidades.

# Creamos instancias de Personaje
goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 99, 99)
jiren = Personaje("Jiren", 130, 140)

# Fusionamos personajes para formar Gogeta y Jireta
gogeta = goku + vegeta
jireta = gogeta + jiren

# Imprimimos la información de los personajes
print(gogeta)
print(jireta)
print(goku)
print(vegeta)
