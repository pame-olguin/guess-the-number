from logica_juego import generar_numero_secreto
from jugador import turno_jugador
from ordenador import turno_ordenador

def juego():
    numero_secreto = generar_numero_secreto()
    tentativas_jugador = []
    print("\n*********BIENVENIDO AL JUEGO GUESS THE NUMBER*******\n")
    print("\n¡Comienza el juego de adivinanza!\n")

    while True:
        # Turno del jugador
        if turno_jugador(numero_secreto, tentativas_jugador):
            print(f"\n¡Felicidades!el jugador ha ganado. Intentos: {tentativas_jugador}\n")
            break

        # Turno del ordenador
        if turno_ordenador(numero_secreto):
            print("\nEl ordenador ha ganado.\n")
            break

if __name__ == "__main__":
    juego()

