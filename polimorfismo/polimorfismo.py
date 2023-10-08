class Gato():
    def sonido(self):
        return "Miau"  # Devolvemos el sonido característico del gato

class Perro():
    def sonido(self):
        return "Guao"  # Devolvemos el sonido característico del perro

def hacer_sonido(animal):
    print(animal.sonido())  # Imprimimos el sonido del animal usando el método sonido

# Creamos instancias de Gato y Perro
gato = Gato()
perro = Perro()

# Llamamos a la función hacer_sonido con un gato y un perro
hacer_sonido(gato)  # Imprime "Miau"
hacer_sonido(perro)  # Imprime "Guao"

# También podemos llamar al método sonido directamente
print(gato.sonido())  # Imprime "Miau"
print(perro.sonido())  # Imprime "Guao"
