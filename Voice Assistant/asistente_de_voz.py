import re
import pyttsx3
import speech_recognition as sr

def initialize_engine():
  
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")
    
    return engine


def recognizer_voice(r):
  
   with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
   return text
        
        
def identify_name(text):
  name = None
  patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
  for pattern in patterns:
      try:
        name = re.findall(pattern, text)[0]
      except IndexError:
        pass
  return name
     
    

def main():
  
    engine = initialize_engine()
    
    engine.say("Hola como te llamas")
    engine.runAndWait()

    r = sr.Recognizer()

    text = recognizer_voice(r)
    name = identify_name(text)
   
    if name:
        engine.say("Encantado de conocerte, {}".format(name))
    else:
          engine.say("Pues mira la verdad que no te entiendo")
    engine.runAndWait()
            
        
if __name__ == "__main__":
    main()