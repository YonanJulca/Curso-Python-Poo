class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre    # Asigna el nombre de la persona
        self.edad = edad        # Asigna la edad de la persona
        self.nacionalidad = nacionalidad  # Asigna la nacionalidad de la persona
        
    def hablar(self):
        print("Hola estoy hablando un poco")  # Imprime un mensaje indicando que la persona está hablando


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)  # Llama al constructor de la clase padre
        self.trabajo = trabajo   # Asigna el trabajo del empleado
        self.salario = salario   # Asigna el salario del empleado


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)  # Llama al constructor de la clase padre
        self.notas = notas       # Asigna las notas del estudiante
        self.universidad = universidad  # Asigna la universidad del estudiante
       

roberto = Empleado("Yonan", 34, "Perú", "Programador", 1000)  # Crea un objeto Empleado llamado "roberto" con ciertas características

roberto.hablar()  # Llama al método hablar() del objeto "roberto"
