class MiClase:
    def __init__(self):
        self.__satributo_privado = "valor"  # Atributo privado

    def __hablar(self):  # Método privado
        print("hola, como estas")

objeto = MiClase()

# Intentamos acceder al atributo privado, pero esto fallará porque el nombre ha sido renombrado
# Usamos el nombre renombrado "_MiClase__satributo_privado" en su lugar
print(objeto._MiClase__satributo_privado)  # Imprime "valor"

# Intentamos llamar al método privado, de nuevo usando el nombre renombrado
objeto._MiClase__hablar()  # Imprime "hola, como estas"
