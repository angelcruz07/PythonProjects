#Minijuego Boss Final 1 Curso de master mind

import random

#Variables
titulo = ("Bienvenido al Mini Juego el escape de Milo")
piedra = ("no ha reccoidgo nada")
num = random.randint(1,10)


print ("\n" + titulo + '\n' +  '-' * len(titulo) + "\n")

print("""Milo se encontraba en una liana cuando por accidente
        resbalo y callo a una cueva donde quedo inconsiente, 
       uando desperto se encontraba dentro de una cueva ayuda a milo a salir de la cueva. \n""")

play = input("¿Quieres ayudar a milo a Salir de la cueva s/n ? \n")

if play == "s":
    print("""Comenzamos el juego \n
             Milo alcanza aver una entrada de luz lo que lo hace suponer que es la salida,
             cuando avanza se encuentra con dos tuneles
             (a) uno se ve bastante tranquilo y llamativo
             (b) el otro es bastante tenebrosa """)

    camino = input("¿Por cual camino quieres guiar a milo a/b ? ")

#Camino 1 Opcion Larga
    if camino == "a":
        print("""Bien vamos por el camino llamativo, 
                 milo avanza dentro del tunel 
                 y se encuentra con otra cueva llena de gemas donde al centro se encuentra
                 una piedra preciosa ,parece mistica \n """)

        #El usuario toma la piedra decisivo para ganar el minijuego

        piedra = input("¿Quieres que milo tome la piedra s/n")

        print("""Milo continua caminando... 
                 depronto comienzan a caer piedras del
                 techo la cueva se esta derrumbando \n""")
        # Hay un derrumbe en la cueva

        #Escapar del del derrumbe
        derrumbe = input("""¿Que deberia hacer milo?
                             a)Correr y buscar salida
                             b)Buscar refugio""")

        if derrumbe == "a":
            print("Milo ha muerto aplastado con una roca, has perdido")
            exit()

        elif derrumbe == "b":
            print("El derrumbe a terminado milo a salido sano y salvo")

            salida_uno = input("""milo ve un tunel y entra dentro de el,
                     ha encontrado a un buho mistico y le pregunta si no tiene 
                     la piedra del dragon lo ayudara a salir 
                     a) Darle la piedra
                     b) No tengo la piedra""")

        #Primera salida de la cueva
        if salida_uno == "a" and piedra == "s":
            print("Milo le da la piedra al buho, este lo ayuda y al fianl milo puede salir de la cueva \n "
                  "***  Felicidades has ganado el minijuego ***")
#Aunque milo seleccione a o b y no tiene ninguna la piedra no podra salir

        elif salida_uno == "b" or salida_uno == "a" and piedra == "n":
            print("Milo no tiene la piedra, siguio con su camino pero jamas logra salir \n"
                  "Has perdido el juego")
            exit()
        else:
            print("No has selecionado ni una opcion, has perdido")
            exit()




#Camino 2 Opcion Corta

    elif camino == "b":
        print("Bien vamos por el camino tenebroso... \n "
              "Milo ha avanzado y se encuentra con una manada de murciélagos.\n"
              "Estos le ofrecen ayuda para salir, pero antes Milo debe responder la siguiente operación.\n")
        operacion = int(input("Un murciélago le pregunta a Milo cuánto es 1 * {}: ".format(num)))

        if operacion == 1 * num:
            print("Tu respuesta es correcta, pero no nos gustan los cerebritos.\n"
                  "Los murciélagos atacan a Milo hasta que este muere...\n"
                  "Milo ha muerto, has perdido el juego.")
            exit()
        elif operacion != num:
            print("Has fallado, perfecto, odiamos a los cerebritos.\n"
                  "Los murciélagos llevan a Milo fuera de la cueva y este puede regresar a casa.\n"
                  "*** Felicidades, has ganado el juego ***")
            exit()
        else:
            print("No has seleccionado ninguna respuesta válida, has perdido.")
            exit()
    else:
        print("No has elegido una respuesta válida, has perdido.")
        exit()
else:
    print("Gracias por jugar. ¡Hasta la próxima!")

