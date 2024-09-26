import time
from colorama import Fore

def turno_jugador(nombre, numero_secreto, tentativas_jugador):
   
    intento = int(input( Fore.YELLOW +"\n" +f"{nombre}, Adivina un número entre 1 y 100: "))
    print("Procesando...")
    time.sleep(2)

    if intento < 1 or intento > 100:
       print("Por favor, ingresa un número entre 1 y 100.")
       return False
    
    tentativas_jugador.append(intento)

    if intento == numero_secreto:
        print("\n"+"¡Has adivinado el número!"+"\n")
        return True
    elif intento < numero_secreto:
        print("\n"+"El número secreto es MAYOR."+"\n")
    else:
        print("\n"+"El número secreto es MENOR."+"\n")
    
    return False