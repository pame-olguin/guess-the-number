from colorama import Fore, Style, init
from logica_juego import generar_numero_secreto
from jugador import turno_jugador
from ordenador import turno_ordenador

init(autoreset=True)

def juego():
    numero_secreto = generar_numero_secreto()
    tentativas_jugadora = []

    print(Fore.MAGENTA + Style.BRIGHT + "\n*********BIENVENIDO AL JUEGO GUESS THE NUMBER*******\n")
    print("\n¡Comienza el juego de adivinanza!\n")

    while True:
        # Turno del jugador
        if turno_jugador(numero_secreto, tentativas_jugadora):
            print(Fore.MAGENTA + Style.BRIGHT + f"\n¡Felicidades! El jugador ha ganado. Intentos: {tentativas_jugadora}\n")
            jugar_de_nuevo = input(Fore.CYAN + "¿Quieres jugar de nuevo? (sí/no): ").lower()
            if jugar_de_nuevo != 'si':
                print(Fore.YELLOW + "\nGracias por jugar. ¡Hasta la próxima!")
                break  # Salir del bucle y terminar el juego
            else:
                numero_secreto = generar_numero_secreto()  # Genera un nuevo número para la próxima partida
                tentativas_jugadora = []  # Reiniciar las tentativas del jugador

        # Turno del ordenador
        if turno_ordenador(numero_secreto):
            print(Fore.MAGENTA + Style.BRIGHT + "\nEl ordenador ha ganado.\n")
            jugar_de_nuevo = input(Fore.CYAN + "¿Quieres jugar de nuevo? (sí/no): ").lower()
            if jugar_de_nuevo != 'sí':
                print(Fore.YELLOW + "Gracias por jugar. ¡Hasta la próxima!")
                break  # Salir del bucle y terminar el juego
            else:
                numero_secreto = generar_numero_secreto()  # Genera un nuevo número para la próxima partida
                tentativas_jugadora = []  # Reiniciar las tentativas del jugador

if __name__ == "__main__":
    juego()