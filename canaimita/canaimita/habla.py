from cgitb import text
from gtts import gTTS
import os

def habla(texto):
  language = "es-us"
  print("Funciona y el texto es:", texto)
  print(os.getcwd())
  speech = gTTS(text=texto, lang=language, slow=False)
  speech.save('C:/Users/PC/Desktop/ProjectJimmy/canaimita/canaimita/static/canaimita/texto.mp3')
  speech.save('texto.mp3')
  #os.system('start texto.mp3')
