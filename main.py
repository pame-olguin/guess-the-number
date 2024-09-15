from utilidades import generar_numero_secreto
from jugador import turno_jugador
from ordenador import turno_ordenador

def juego():
    numero_secreto = generar_numero_secreto()
    tentativas_jugador = []
    print("¡Comienza el juego de adivinanza!")

    while True:
        # Turno del jugador
        if turno_jugador(numero_secreto, tentativas_jugador):
            print(f"El jugador ha ganado. Intentos: {tentativas_jugador}")
            break
        # Turno del ordenador
        if turno_ordenador(numero_secreto):
            print("El ordenador ha ganado.")
            break
        
