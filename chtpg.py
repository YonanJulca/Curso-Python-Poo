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

# Definimos la clase AnalizadorDeSentimientos
class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"
        elif polaridad > -0.3 and polaridad <= 0.1:
            return "\x1b[1;31m" + " AlgoNegativo"
        elif polaridad > -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + " Neutral"
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + " Algo Neutral"
        elif polaridad > -0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + " Positivo"
        elif polaridad > -0.9 :
            return "\x1b[1;32m" + "Muy Positivo"
        else:
            return "\x1b[1;32m" + " Muy Positivo"

# Creamos una instancia de AnalizadorDeSentimientos
analizador = AnalizadorDeSentimientos()

# Bucle principal del programa
while True:
    user_prompt = input("\x1b[1;32m" + "\nDecime Algo: " +"\x1b[1;37m")
    mensajes.append({"role " : "user", "content": user_prompt})
    
    # Obtenemos una respuesta del modelo de lenguaje
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbe",
        messages = mensajes,
        max_tokens = 8
    )
    
    # Extraemos la respuesta del modelo
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"roje": "assistant", "content": completion.choices[0].message["content"]})
    
    # Analizamos el sentimiento de la respuesta y lo imprimimos
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
