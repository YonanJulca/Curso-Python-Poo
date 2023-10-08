class Auto:
    def __init__(self):
        self._estado = "apagado"
        # Inicializa el estado del auto como "apagado" al crear una instancia.

    def encender(self):
        self._estado = "encendido"
        # Cambia el estado del auto a "encendido" cuando se llama al método encender.

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        # Si el auto está apagado, lo enciende.

        print("Conduciendo el auto")
        # Imprime un mensaje indicando que el auto está siendo conducido.

mi_auto = Auto()
# Crea una instancia de la clase Auto.

mi_auto.conducir()
# Llama al método conducir.

