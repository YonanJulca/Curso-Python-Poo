# Definimos una clase base Notificador
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        # Este método será implementado por las subclases
        raise NotImplementedError

# Definimos una subclase NotificadorEmail que hereda de Notificador
class NotificadorEmail(Notificador):
    def notificar(self):
        # Enviamos un mensaje por correo electrónico al usuario
        print(f"Enviando mensaje por mail a {self.usuario.email}")

# Definimos una subclase NotificadorSMS que hereda de Notificador
class NotificadorSMS(Notificador):
    def notificar(self):
        # Enviamos un mensaje de texto al usuario
        print(f"Enviando SMS a {self.usuario.sms}")

# Definimos una subclase NotificadorWhatsapp que hereda de Notificador
class NotificadorWhatsapp(Notificador):
    def notificar(self):
        # Enviamos un mensaje por WhatsApp al usuario
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")
