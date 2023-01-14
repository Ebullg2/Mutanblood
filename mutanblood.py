#        MODULOS
from time import sleep 
import os 
import sys

#        VARIABLES
 
historia_de_la_guerra = """...... 25 de abril del año 2092...
 
    El año 2087 marco el comienzo de la 6ta guerra mundial. El conflicto no se
 limito a una zona geografica o a un grupo de paises, si no que involucro
 a la mayoria de los estados del mundo. Estados unidos, China, Japon, 
 Alemania, Francia, Italia, Reino unido, Rusia, Argentina, Iran, y el estado de israel
 eran los principales contendientes.

 Las tensiones entre los paises se habian estado acumulando durante los
 ultimos años, pero la situacion se volvio insostenible a principio de
 2087 cuando los lideres de varios paises se reunieron en una conferencia
 de paz en la ONU. Los intentos de llegar a un acuerdo fracasaron y, como
 resultado, los paises comenzaron una guerra.

 Los primeros dias de la guerra fueron dificiles para ambos lados. Estados 
 Unidos, China, Japon y Europa occidental lanzaron ataques militares contra 
 los estados enemigos. Los ataques incluyeron bombardeos aereos,
 operacioes terrestres y maritimas, y el uso de armas nucleares y quimias.
 Rusia, Iran y el Estado de Israel lanzaron ataques similares.

 Los combates se extendieron por todo el mundo durante los siguientes cinco
 años. Los paises lucharon por el control de territorios, recursos y poder.
 Durante este tiempo y terminaron destruyendose, millones de personas 
 murienron y otras mutaron junto con algunos animales,
 el destino del mundo se puso en juego. Quedando menos del 40% de la
 poplacion mundial...

 Diario: Comandante Gonzales Eduardo. """
 
historia_de_lo_sucedido = """......3 de OCTUBRE del año 2092...
 
    Despues de la 6ta guerra mundial, el mundo ya no era lo mismo. las ciudades
 estaban en ruinas, el caos y las destruccion era la normal, la humanidad estaba
 al borde de la extincion. Los sobrevivientes que quedaron tuvieron que hacer 
 frente a un nuevo enemigo: los mutantes creados por la radiacion
 de las armas nucleares. Estos monstruos eran mas fuertes, mas peligrosos y mas 
 sedientos de sangre que cualquier ser humano.

   Los supervivientes se vieron obligados a esconderse en antiguos bunkers y 
 refugios para mantenerse a salvo de los mutantes. Muchas personas murieron 
 intentando combatir a los monstruos, mientras que otras tuvieron que hacerse la 
 idea de que el mundo que conocian habia desaparecido para siempre.

   finalmente, los pocos supervivientes que quedaron intentaron unir fuerzas
 para combatir a los mutantes. Armas y estrategias especiales fueron desarrolladas
 para contrarrestar a los monstruos, pero fracasaron horriblemente teniendo 
 miles de perdidas..............."""

estado_actual =  """
    Eres un{} de los pocos sobrevivientes, pero estas atrapado
  un edificio rodeado de mutantes. Colocaste una barricada en la puerta principal 
  con lo primero que encontraste, aun asi no es suficiente, tienes que subir a 
  lo alto del edificio para llegar a un helicoptero que esta en el techo y poder huir."""
edad   = None
nombre = None
genero = None
v      = 0.7
maso_de_hierro = False
cuerda         = False
machete        = False
palo_con_clavo = False 
barra_metal    = False
list_pisos = ["PB", "P1", "P2", "P3"]

#          JUEGO    

print("\n                 BIENVENIDO A MI JUEGO \n      "
       "ANTES DE EMPEZAR, HABLAME UN POCO DE TI\n")

while edad == None: # esta while esta para que no tengas que iniciar el programa de
    edad = int(input("¿Cuantos años tienes?: "))

    if edad <= 16:
        print("Lo siento, eres menor de edad.")
        edad = None

    elif 60 <= edad:
        print("no mames, tampoco asi.")
        edad = None

nombre = input("¿Como te llamas?: ")

while genero != "M" and genero != "m" and genero != "F" and genero != "f": # ya que genero no es nada entra en la while
    genero = input("¿Eres Chico[M] o Chica[F]?: ") # aqui, guarda tu genero en la variable para usarlo mas tarde

    if genero != "M" and genero != "m" and genero != "F" and genero != "f":# aqui comprueba si usaste las opciones puestas 
        print("Las unicas opciones son F y M.")

if genero == 'f' or genero == 'F':
    genero = 'a'
elif genero == 'm' or genero == 'M':
    genero = 'o'

os.system("cls" if os.name == "nt" else "clear")

for e in historia_de_la_guerra:
    print(e, end="")
    sys.stdout.flush()
    sleep(0.1)

for e in historia_de_lo_sucedido:
    print(e, end="")
    sys.stdout.flush()
    sleep(0.1)
 
sleep(5)
 
print(f"\n ¿Estas list{genero}? ahora empieza lo bueno\n")

for e in estado_actual.format(genero):
    print(e, end="")
    sys.stdout.flush()
    sleep(0.1)

print("\n¿Por donde pinsas subir?")
opcion = input( "A - Escaleras.\n"
                "B - Acensor.\n ¬ ")

os.system("cls" if os.name == "nt" else "clear")

if opcion == "A" or opcion == "a":
    print(
        "\nSubes las escaleras corriendo lleguando al 3er piso,\n"
        "de repende escuchas los gritos y paso de los mutantes siguiendote\n")
    opcion = input(
        "¿Que haces?\n"
        "A - Siguo subiendo las escaleras\n"
        "b - Me detengo y entro a la puerta del 3er piso\n ¬ ")
    
    os.system("cls" if os.name == "nt" else "clear")

    if opcion == "A" or opcion == "a":
        print("Subes lo mas rapido, pero los mutantes te atrapan y te descuartisan y mueres.")
        print("GAME OVER")
        exit()

    elif opcion == "B" or opcion == "b":
        print("Pasas la puerta del 3er piso y ves en el suelo una barra de metal.")
        opcion = input(
            "¿Que haces?\n"
            "A - Cojo la barra de metal y tranco la puerta\n"
            "B - Siguo corriendo\n ¬ ")
        
        os.system("cls" if os.name == "nt" else "clear")

        if opcion == "A" or opcion == "a":
            print(
                "\nCierro la puerta con la ayuda de la barra, escuchas como "
                "los mutantes tratan de derribar la puerta, 5 monstruos "        
                "entran por un agujero en el suelo, y comienza de nuevo la persecucion.\n")
            barra_metal = True 

        elif opcion == "B" or opcion == "b":
            print("\nMarcas la milla y sigues corriendo, los monstruos pasan por la puerta.\n")

        else:
            print("Las opciones validas son A y B")
            exit()
        
        print(
            "Llegas al final del pasillo y hay dos puertas, tienes que tomar una desicion rapida,"
            "una te ayudara a ir al siguiente piso, otra te llevara a una horrible y dolorosa muerte.\n")
        opcion = input("¿Que habiacion eliges?\n"
                       "A - Derecha.\n"
                       "B - Izquierda.\n ¬ ")
        
        os.system("cls" if os.name == "nt" else "clear")

        if opcion == "A" or opcion == "a":
            print(
                "\nEntras en la puerta de la derecha, cierras con seguro y trancas la puerta"
                "con el muebles de al lado, los mutantes tratan de entar"
                f"decesperad{genero} ves a todas la direcciones, logras divisar 2 jarras llenos de gasolina,"
                "una pequeña bombona medio llena, un mechero y una ventana que lleva a unas escaleras. \n")
            opcion = input(
                "\n¿Que haces?\n"
                "A - Baño la habitacion de gasolina con las 2 jarras, abro la bombona y enciendo el mechero.\n"
                "B - Baño la habitacion de gasolina con una jarra, abro la bombona,\n"
                " salgo por la ventana haciendo un camino de gasolina con la otra jarra.\n" 
                "C - Salgo por la ventana.\n ¬ ")
            
            os.system("cls" if os.name == "nt" else "clear")

            if opcion == "A" or opcion == "a":
                print(
                    "\nBañas la habitacion de gasolina con las 2 jarras, abro la bombona "
                    "los mutantes destrosan la puerta, enciendes el mechero, mandas a volar a los mutantes pero mueres.")
                print("GAME OVER.")
                exit()

            elif opcion == "B" or opcion == "b":
                print(
                    "Bañas la habitacion de gasolina con una jarra, abro la bombona, "
                    "salgo por la ventana haciendo un camino de gasolina con la otra jarra, los mutantes destrosan "
                    "la puerta, rapidamente encienes el camino de gasolina, el camino de fuego al llegar a la "
                    "ventana la bombona explota, mandando a volar a miles de monstruos y parte del 3er y 4to piso"
                    "mientras tu estas asalvo en el 5to piso.")

                print("Empiezas a bailar epicamente....")

                print(
                    "Mientras demuestras tus pasos prohibidos logras ver por la ventana una ola de mutantes acercandose "
                    "llamodos por la explocion que causaste...\n"
                    "Aprovechas rapidamente y subes las escaleras.\n")

                if barra_metal == True:
                    print(
                        "Llegas al techo, y te encuentras con decenas de mutantes.\n"
                        "Gritas: ¡¡ALV!!\n"
                        "Llamando la atencion de estos te ven y te matan.\n")
                    print("GAME OVER")
                    print("APORTACION:resulta que al cerras la puerta de las escaleras, estos siguieron subiendo hasta lleguar al techo.")
                    exit()
                else:
                    print("Llegas al techo, te subes al helicoptero, te vas volando y te burlas epicamente de los mutantes.")
                    print("FIN.")
                    exit()

            elif opcion == "C" or opcion == "c":
                print("Sales por la ventana, los mutantes destrosan la puerta te encuentran y te matan.")
                print("GAME OVER")
                exit()  

            else:
                print(
                    "Llegas al techo, te subes al helicoptero, te vas volando y "
                    "te burlas epicamente de los mutantes.")
                print("FIN.")
                exit()      
                          
        elif opcion == "B" or opcion == "b":
            print(
                "Entras en la puerta de la derecha, cierras con seguro y trancas la puerta "
                "con el muebles de al lado, los mutantes tratan de entar... "
                "Al darte la vuelta te encuentras con una traumante vista, decenas de cadaveres "
                "decuartisados pudriendose... Te tomas un momento, "
                f"decesperad{genero} ves a todas la direcciones y encuentras un agujero en el techo, "
                "tomas una mesa y subes llegando al 4to piso, pero los mutantes derriban la puerta "
                "tratas de correr pero te atrapan y mueres." )
        
        else:
            print("Las opciones validas son A y B")

    else:
        print("Las opciones validas son A y B")

elif opcion == "B" or opcion == "b":
    print(  
        "Decides subir por el ascensor, pero cuando se abrieron las puertas, viste que los mutantes "
        f"habian traspasado la puerta principal, entras al ascensor y decesperad{genero} precionas el "
        "boton de subir multiples veces. "
        f"la puerta se cierra, {nombre} ya asalv{genero} se tranquiliza, le das al boton del ultimo"
        " piso y el ascensor comienza a subir.\n")
    
    for item in list_pisos:
        print(item)
        sleep(1.5)
    
    print(       
        "De repente el ascensor se detiene entre el 3er piso y el 4to, abres las puertas pero lo que ves "
        "es un muro de cemento.\n"
        "\n¿Que haras?")
    opcion = input(
        "A - Esperar ayuda\n"
        "B - subir por la escotilla superior\n ¬ ")
    
    os.system("cls" if os.name == "nt" else "clear")

    if opcion == "A" or opcion == "a":
        print(
            "Esperas pacientemente a que alguien te venga a rescatar, a los pocos minuros el elevando se empieza a mover"
            "se desprende el techo de este y te caen encima miles de mutantes aplastandote.")
        exit()

    elif opcion == "B" or opcion == "b":
        print(
            "Subes por la escotilla del elevador y frente de ti esta la puerta del 4to piso"
            "de lo alto escuchas los cables del elevador desprendiendoce, te apresuras a abrir la puerta"
            "usando todas tus fuerzas la abres y logras salir antes de que el ascensor caiga.\n")

        print(
            "Los mutantes lleguan al piso en donde estas, empizas a correr con todas lo que tienes, llegando al final "
            "del pasillo, a la izquierda tienes una puerta, al frente una agujero que lleva al exterior.\n"
            "¿Que haces?\n")
        opcion = input(
            "A - Izquierda\n"
            "B - Siguo derecho \n ¬ ")
        
        os.system("cls" if os.name == "nt" else "clear")

        if opcion == "A" or opcion == "a":
            print(
                "Entras en la habitacion, cierras la puerta y la trancas con lo primero que encuentras.\n "
                'Los monstruos tratan de entrar.\n '
                '¿Que haces?\n')
            opcion = input(
                "A - Pienso en una solucion\n"
                "B - Me decespero\n"
                "C - Me escondo\n ¬ ")
            
            os.system("cls" if os.name == "nt" else "clear")

            if opcion == "A" or opcion == "a":
                opcion = input(
                    "Analizas la situacion.\n  "
                    "A - Busco algo en el cuarto que pueda servirme\n"
                    "B - Me decespero\n ¬ ")
                
                os.system("cls" if os.name == "nt" else "clear")

                if opcion == "A" or opcion == "a":
                    print(
                        "Buscas en el cuarto cualquier cosa que pueda ayudarte, encuentras un maso de hierro,"
                        "una machete, una cuerda y un palo con un clavo.\n"
                        "Escuchas como los mutantes estan decesperados para entrar.\n"
                        "¿Que haces? \n")
                    opcion = input(
                        "A - Pienso en una solucion\n"
                        "B - Agarras un Arma para defenderte\n ¬ ")
                    
                    os.system("cls" if os.name == "nt" else "clear")

                    if opcion == "A" or opcion == "a":
                        input(
                            "Analizas la situacion...\n"
                            "A - Busco una forma de huir\n"
                            "B - Me decespero\n ¬ " )
                        
                        os.system("cls" if os.name == "nt" else "clear")

                        if opcion == "A" or opcion == "a":
                            print(
                                "Buscas en toda la habitancion por donde escapar, y te encuentras con el ducto de ventilacion."
                                "Escuchas como los mutantes estan decesperados para entrar"
                                "¿Que haces? ")
                            opcion = input(
                                "A - Agarro un arma y me defiendo\n"
                                "B - Agarro un arma y salgo por el conducto\n"
                                "C - salgo por el conducto\n ¬ ")
                            
                            os.system("cls" if os.name == "nt" else "clear")

                            if opcion == "A" or opcion == "a":
                                opcion = input(
                                    "¿Elige sabiamente?\n"
                                    "A - El Maso de hierro\n"
                                    "B - El machete\n"
                                    "C - La cuerda\n"
                                    "D - El palo con el clavo\n ¬ ")
                                
                                os.system("cls" if os.name == "nt" else "clear")

                                if opcion == "a" or opcion == "b" or opcion == "c" or opcion == "d":
                                    print(
                                        "Los mutantes entran."
                                        "Coges tu armas y te preparas para una sangrienta batalla."                                           
                                        "Los mutantes se lanzan contra ti, pero son muchos, te descuartizan y mueres.\n")
                                    print("GAME OVER")
                                    exit() 

                                else:
                                    print("Ninguna de las opciones son validas")
                                    exit()
                            
                            elif opcion == "B" or opcion == "b":
                                opcion = input(
                                    "¿Elige sabiamente?\n"
                                    "A - El Maso de hierro\n"
                                    "B - El machete\n"
                                    "C - La cuerda\n"
                                    "D - El palo con el clavo\n ¬ ")
                                
                                os.system("cls" if os.name == "nt" else "clear")

                                if opcion == "A" or opcion == "a":
                                    maso_de_hierro = True
                                    objeto = "el Maso de hierro"

                                elif opcion == "B" or opcion == "b":
                                    machete = True
                                    objeto = "el machete"

                                elif opcion == "C" or opcion == "c":
                                    cuerda = True
                                    objeto = "la cuerda"

                                elif opcion == "D" or opcion == "d":
                                    palo_con_clavo = True
                                    objeto = "el palo con el clavo"
                                                                  
                                else:
                                    print("Las opciones validas son A, B, C y D.")
                                    exit()

                                # Esto ayudara mas adelante, para decidir que pasa en e conducto.
                                objeto_invetario = True 
                                pierdes_los_mutantes = True 

                            elif opcion == "C" or opcion == "c":
                                pierdes_los_mutantes = True 
                            # Decoracio XD na mentira. esta if permine continuar el juego

                            else:
                                print("Las opciones validas son A, B y C")
                                exit()
                            
                            print("Abres la ventilacion y huyes.")
                            print(
                                "Logras perder a los mutantes, sigue pasiando buscan el camino que te lleve al techo "
                                "por el ducto silenciosamente, pasas por el 5to piso, tratas de no llamar la atencion "
                                "y sigues tu camino, lleguas al techo, pero el ducto esta tapado y no puedes salir.\n")

                            if pierdes_los_mutantes == True and objeto_invetario != True:
                                print(
                                    "No tienes que con abrir el ducto, y si regresas al cuarto los mutantes te mataran."
                                    "No tienes otra opcion que ir al 5to piso a buscar una solicion, pero hay mutantes en todo el piso "
                                    "y no logras nada."
                                    "No tines como abrir el ducto, no tienes nada que te ayude, y a los dias mueres de hambre.")
                                print("GAME OVER")
                                exit()

                            else:
                                opcion = input(
                                    "¿Que haces?\n"
                                    "A - Abro el ducto con el objeto que llevo\n"
                                    "B - Me regreso al 5to piso\n ¬ ")
                                
                                os.system("cls" if os.name == "nt" else "clear")
                                
                                if opcion == "A" or opcion == "a":
                                    print(
                                        f"No puedes usar {objeto} ya que es muy estrecho."
                                        "No tienes otra opcion que regresar al 5to piso.\n")

                                elif opcion == "B" or opcion == "b":
                                    print("Retrocedes con cuidado.")

                                else:
                                    print("Las opciones validas son A y B")
                                    exit()
                                
                                print(
                                    "Ya estando en este, Buscas otra forma de ir al techo."
                                    "Al cabo de un rato encuentras 2 formas de ir al techo, en un cuarto hay un mutante bloquean "
                                    "una puerta que lleva al techo, y en el otro hay una llave que abre la puerta de las escaleras"
                                    "pero esta lleno de mutantes dormidos. "
                                    "Tienes 2 opciones:")
                                
                                opcion = input( 
                                    "A - Voy por la llave\n"
                                    "B - Voy por la puerta bloqueada\n ¬ ")
                                
                                os.system("cls" if os.name == "nt" else "clear")
                                
                                if opcion == "A" or opcion == "a":
                                    print(
                                        "Te diriges para donde esta la llave."
                                        "Al llegar al cuarto, logras ver desde el ducto la llave, rodeada de mutantes dormidos"
                                        "¿que haces?")
                                    opcion = input(
                                        "A - Uso el objeto que tengo para alcanzarla\n "
                                        "B - Tratas de alcanzarla con la mano\n ¬ ")
                                    
                                    os.system("cls" if os.name == "nt" else "clear")
                                    
                                    if opcion == "A" or opcion == "a":
                                        print(f"Usas {objeto} y con cuidado tratas de alcanzar la llaves.")

                                        if palo_con_clavo == True:
                                            print(
                                                "¡Lo lograste!, tienes la llave, ahora vas y abres la puerta."
                                                "Llegas al techo, corres a donde esta el helicoptero y te vas volando. "
                                                "WINNER")
                                            exit()
                                        else:
                                            print(
                                                f"Tratas de alcanzar la llave, pero se te cae {objeto} despertando "
                                                "a los monstruos, estos te encuentran y te matan."
                                                "GAME OVER")
                                            exit()

                                    elif opcion == "B" or opcion == "b":   
                                        print(
                                            "Tratas de alcanzara con la mano y te caes, despertando a los mutantes."
                                            "Estos te ven y te matan."
                                            "GAME OVER")
                                        exit()                                
                                    
                                    else:
                                        print("Las opciones validas son A y B")
                                        exit()

                                elif opcion == "B" or opcion == "b":
                                    print(
                                        "Te diriges para donde esta el mutante."
                                        "Ya estando cerca de el, te das cuenta que tu unica salida es peliar, "
                                        f"tomas {objeto}, te preparas y sales del ducto con {objeto} en mano.")
                                    
                                    if cuerda == True:
                                        print(
                                            "caes sobre el mutante, con ayuda de la cuerda le haces imposible respirar, "
                                            "a los pocos segundos cae al suelo y muere.")
                                    else:
                                        print( 
                                            "golpeas al mutante en la cabeza, pero le diste tan fuerte al mutante"
                                            "que lo mataste.")
                                    
                                    print(
                                        "¡Lo lograste!, ahora vas abres puerta.\n"
                                        "Llegas al techo, corres a donde esta el helicoptero y te vas volando.\n "
                                        "¡WINNER!")
                                    exit()
                                
                                else:
                                    print("Las opciones validas son A y B")
                                    exit()
                            
                        elif opcion == "B" or opcion == "b":
                            print("Entras en panico, los mutantes derriban la puerta y te matan.\n")
                            print("GAME OVER")
                            exit()

                        else:
                            print("las opciones validas son A y B")
                            exit()

                    elif opcion == "B" or opcion == "b":
                        opcion = input(
                            "¿Elige sabiamente?\n"
                            "A - El Maso de hierro\n"
                            "B - El machete\n"
                            "C - La cuerda\n"
                            "D - El palo con el clavo\n ¬ ")
                        
                        os.system("cls" if os.name == "nt" else "clear")

                        if opcion == "a" or opcion == "b" or opcion == "c" or opcion == "d":
                            print(
                                "Los mutantes entran.\n"
                                "Coges tu armas y te preparas para una sangrienta batalla.\n"                                           
                                "Los mutantes se lanzan contra ti, pero son muchos, te descuartizan y mueres.\n")
                            print("GAME OVER")
                            exit() 
                    
                    else:
                        print("Las opciones validas son A y B")
                        exit()

                elif opcion == "B" or opcion == "b":
                    print("Entras en panico, los mutantes derriban la puerta y te matan.")
                    print("GAME OVER")
                    exit()

                else:
                    print("Las opciones validas son A y B")
                    exit()
            
            elif opcion == "B" or opcion == "b":
                print("Entras en panico, los mutantes derriban la puerta y te matan.")
                print("GAME OVER")
                exit()
                
            elif opcion == "C" or opcion == "c":
                print("Decides esconderte, los mutantes derriban la puerta, te encuentran y mueres.")
                print("GAME OVER")
                exit()

            else:
                print("Las opciones validas son A, B y C")
                exit()


        elif opcion == "B" or opcion == "b":
            print(
                "Te lanzas por el agujero en frente de ti, y empiezas a caer desde el 4to piso hasta la calle"
                "mueres por la caida"
                "GAME OVER")
            exit()

        else:
            print("Las opciones validas son A y B")
            exit()

    else:
        print("Las opciones validas son A y B")
        exit()

else:
    print("Las opciones validas son A y B")
    exit()