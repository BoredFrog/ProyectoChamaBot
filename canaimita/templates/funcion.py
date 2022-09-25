from cgitb import text
from gtts import gTTS
import os

def habla():
  text= "Hola Jimmy. presentas fuerte inclinaciones por expresiones artísticas. Tienes marcados totes musicales y se te daría bien la actuación"
  language = "es-us"

  speech = gTTS(text=text, lang=language, slow=False)
  speech.save('texto.mp3')
  os.system('start texto.mp3')

habla()