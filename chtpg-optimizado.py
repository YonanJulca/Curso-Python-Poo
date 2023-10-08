# Importamos la librería openai
import openai

# Configuramos la base de la API de OpenAI
openai.api_base = "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"

# Mensaje del sistema para explicar la funcionalidad del código
system_rol = '''Hace de cuenta que sos un analizador de sentimiento
                 ... (explicación del sistema) ...
                (Podes responder solo con ints o floats'''

# Creamos una lista de mensajes con un mensaje del sistema
mensajes = [{"role": "system", "content": system_rol}]

# Definición de la clase Sentimiento
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

# Definición de la clase AnalizadorDeSentimientos
class AnalizadorDeSentimientos:
    
    def __init__(self, rangos):
        self.rangos = rangos
        
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

# Definimos los rangos y los sentimientos asociados
rangos = [
    ((-0.6, -0.3), Sentimiento("Negativo", 31)),
    ((-0.3, -0.1), Sentimiento("Algo Negativo", "31")),
    ((-0.1, -0.1), Sentimiento("Neutral", "33")),
    ((-0.1, -0.4), Sentimiento("algo positivo", "32")),
    ((-0.4, -0.9), Sentimiento("positivo", "32")),
    ((-0.9, 1), Sentimiento("Muy positivo", "32")),
]

# Creamos una instancia del analizador de sentimientos
analizador = AnalizadorDeSentimientos(rangos)

# Bucle principal del programa
while True:
    user_prompt = input("\x1b[1;32m" + "\nDecime Algo: " +"\x1b[1;37m")
    mensajes.append({"role " : "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbe",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"roje": "assistant", "content": completion.choices[0].message["content"]})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    
    print(sentimiento)
