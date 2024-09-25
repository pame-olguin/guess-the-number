from random import randint
import time
from colorama import Fore 

def turno_ordenador(numero_secreto, tentativas_ordenador):
    intento = randint(1, 100)
    print(Fore.GREEN + f"\nEl ordenador adivina: {intento}")
    print("Procesando...")
    time.sleep(2)

    tentativas_ordenador.append(intento)

    if intento == numero_secreto:
        print("\nEl ordenador ha adivinado el número." + "\n")
        return True
    
    elif intento < numero_secreto:
        print("\nEl número secreto es mayor.")
    
    else:
        print("\nEl número secreto es menor.")

    return False 
  