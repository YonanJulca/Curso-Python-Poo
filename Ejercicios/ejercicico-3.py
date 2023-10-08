class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El ave está volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando")

class Murcielago(Mamifero, Ave):
    pass

# Creamos una instancia de Ave
ave = Ave()

# Llamamos a los métodos de Ave
ave.comer()  # Esto imprime "El animal está comiendo"
ave.volar()  # Esto imprime "El ave está volando"

# Imprimimos el Orden de Resolución de Métodos (Method Resolution Order) de Murcielago
print(Murcielago.mro())
