import time
from colorama import Fore, Back, Style, init

def turno_jugador(numero_secreto, tentativas_jugador):
    intento = int(input(Fore.BLUE + "\n" +"Adivina un número entre 1 y 100:"))
    tentativas_jugador.append(intento)
    print("Procesando...")
    time.sleep(2)

    if intento < 1 or intento > 100:
       print("Por favor, ingresa un número entre 1 y 100.")
       return False
    
    if intento == numero_secreto:
        print("\n"+"¡Has adivinado el número!"+"\n")
        return True
    elif intento < numero_secreto:
        print("\n"+"El número secreto es MAYOR."+"\n")
    else:
        print("\n"+"El número secreto es MENOR."+"\n")
    
    return False