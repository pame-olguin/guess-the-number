from colorama import Fore, init, Style
from logica_juego import generar_numero_secreto
from jugador import turno_jugador
from ordenador import turno_ordenador

init(autoreset=True)

def juego():
    numero_secreto = generar_numero_secreto()
    print(numero_secreto)
    tentativas_jugadora = []
    tentativas_ordenador = []

    print(Fore.MAGENTA + Style.BRIGHT + "\n*********BIENVENIDO AL JUEGO GUESS THE NUMBER*******\n")
    print("\n¡Comienza el juego de adivinanza!\n")

    while True:
        # Turno del jugador
        if turno_jugador(numero_secreto, tentativas_jugadora):
            print(Fore.MAGENTA + Style.BRIGHT + f"\n¡Felicidades! El jugador ha ganado. Intentos: {tentativas_jugadora}\n")
            jugar_de_nuevo = input(Fore.CYAN + "¿Quieres jugar de nuevo? (si/no): ").lower()
            if jugar_de_nuevo != 'si':
                print(Fore.YELLOW + "\nGracias por jugar. ¡Hasta la próxima!")
                break  # Salir del bucle y terminar el juego
            else:
                numero_secreto = generar_numero_secreto()  # Genera un nuevo número para la próxima partida
                tentativas_jugadora.clear()  # Reiniciar las tentativas del jugador
                tentativas_ordenador.clear() # Reiniciar las tentativas del ordenador

        # Turno del ordenador
        if turno_ordenador(numero_secreto, tentativas_ordenador):
            print(Fore.MAGENTA + Style.BRIGHT + f"\nEl ordenador ha ganado. Intentos: {tentativas_ordenador}\n")
            jugar_de_nuevo = input(Fore.CYAN + "¿Quieres jugar de nuevo? (si/no): ").lower()
            if jugar_de_nuevo != 'si':
                print(Fore.YELLOW + "Gracias por jugar. ¡Hasta la próxima!")
                break  # Salir del bucle y terminar el juego
            else:
                numero_secreto = generar_numero_secreto()  # Genera un nuevo número para la próxima partida
                tentativas_jugadora.clear() # Reiniciar las tentativas del jugador
                tentativas_ordenador.clear() # Reiniciar las tentativas del ordenador

if __name__ == "__main__":
    juego()