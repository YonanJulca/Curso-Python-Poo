# Definición de la clase Celular
class Celular:
    # Constructor de la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca     # Asigna la marca del celular
        self.modelo = modelo   # Asigna el modelo del celular
        self.camara = camara   # Asigna la especificación de la cámara
        
    # Método para simular una llamada
    def llamar(self):
        print(f"Estás haciendo una llamada desde un {self.modelo}")
        
    # Método para simular cortar una llamada
    def cortar(self):
        print(f"Has cortado la llamada de tu {self.modelo}")

# Crear tres instancias de la clase Celular con diferentes especificaciones
celular1 = Celular("Samsung", "s23", "48mp")
celular2 = Celular("Apple", "iPhone 15", "20px")
celular3 = Celular("Huawei", "P40", "64mp")

# Llamar al método llamar de celular1
celular1.llamar()
