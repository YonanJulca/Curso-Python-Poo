# Definición de la clase Estudiante
class Estudiante:
    # Constructor de la clase
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre  # Asigna el nombre del estudiante
        self.edad = edad      # Asigna la edad del estudiante
        self.grado = grado    # Asigna el grado del estudiante
    
    # Método para simular que el estudiante está estudiando
    def estudiar(self):
        print("Estudiando...")

# Solicitar información del usuario
nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado = input("Digame su grado: ")

# Crear una instancia de la clase Estudiante con la información proporcionada
estudiante = Estudiante(nombre, edad, grado)

# Imprimir los datos del estudiante
print(f'''
      Datos Del Estudiante:\n\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}\n
      ''')

# Bucle infinito para permitir que el estudiante estudie repetidamente
while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
       estudiante.estudiar()  # Llama al método estudiar si el usuario escribe "estudiar"
