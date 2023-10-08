# Definimos la clase Ave
class Ave:
    def volar(self):
        return "Estoy volando"

# Definimos la clase Pinguino que hereda de Ave
class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"

# Definimos una función hacer_volar que toma un objeto de tipo Ave y llama a su método volar
def hacer_volar(ave=Ave()):
    return ave.volar()

# Llamamos a hacer_volar con un objeto de tipo Pinguino
print(hacer_volar(Pinguino()))
