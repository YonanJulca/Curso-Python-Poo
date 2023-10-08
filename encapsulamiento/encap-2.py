class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Se inicializa el atributo _nombre con el nombre proporcionado
        self._edad = edad  # Se inicializa el atributo _edad con la edad proporcionada

    def get_nombre(self):
        return self._nombre  # Devuelve el nombre almacenado

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre  # Establece un nuevo nombre

# Creamos una instancia de Persona
yonan = Persona("Yonan", 21)

# Obtener el nombre y imprimirlo
nombre = yonan.get_nombre()
print(nombre)  # Esto imprimirá "Yonan"

# Cambiar el nombre y obtenerlo nuevamente
yonan.set_nombre("Quispe")
nombre = yonan.get_nombre()
print(nombre)  # Esto imprimirá "Quispe"
