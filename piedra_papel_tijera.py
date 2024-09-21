
import random 

# juego de piedra papel y tijera 


# funcion para obtener eleccion del jugador 

def eleccion_jugador():
    
    while True:
        opcion = input("Ingresa una opcion (piedra, papel, tijera): ")
        if opcion.lower() in ["piedra", "papel", "tijera"]:
            return opcion.lower()
        else:
            return "Opcion invalida. Intenta de nuevo."

# para obtener la eleccion de la computadora 
def eleccion_computadora():
    opcion = ["piedra","papel","tijera"]
    return random.choice(opcion)

# determinar las reglas del juego
reglas_juego = {
      "piedra":{"gana_a": "tijera", "piedra_contra": "papel"},
      "papel":{"gana_a": "piegra", "pierde_contra": "tijera"},
      "tijera":{"gana_a": "papel", "pierde_contra": "piedra"}
}

# determinar al ganador 

def determinar_ganador(jugador, computadora, reglas):
    
    if jugador == computadora:
        return "Empate"
    elif reglas[jugador]["gana_a"] == computadora:
        return "Ganaste"
    else:
        return "Perdiste"
    


def jugar ():
    
    while True:
        jugador = eleccion_jugador()
        computadora = eleccion_computadora()
        resultado = determinar_ganador(jugador, computadora, reglas_juego)
        print(f"Elegiste {jugador} y la computadora {computadora}. {resultado}")
        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ")
        if jugar_de_nuevo.lower() != 's':
            break
        
jugar()