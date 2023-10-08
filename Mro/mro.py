class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    pass

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    pass

# Creamos una instancia de la clase D
d = D()

# Imprimimos el Orden de Resolución de Métodos (Method Resolution Order)
print(D.mro())
