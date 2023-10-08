# Importamos la clase TextBlob de la librería textblob
from textblob import TextBlob

# Definimos la clase AnalizadorDeSentimiento
class AnalizadorDeSentimiento:
    def analizar_sentimiento(self, texto):
        # Creamos una instancia de TextBlob para analizar el texto
        analisis = TextBlob(texto)
        
        # Verificamos la polaridad del sentimiento
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"

# Creamos una instancia de AnalizadorDeSentimiento
analizador = AnalizadorDeSentimiento()

# Analizamos el sentimiento del texto "Hola como estas"
resultado = analizador.analizar_sentimiento("Hola como estas")

# Imprimimos el resultado
print(resultado)
