def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funciom")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola Yonan")
    
# saludo_modificado = decorador(saludo)

# saludo_modificado()

@decorador
def saludo():
    print("Hola yonan como estas")
    
    
saludo()