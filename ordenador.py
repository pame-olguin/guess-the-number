import random
import time
from colorama import Fore, Back, Style, init

def turno_ordenador(numero_secreto):
  intento = random.randint(1, 100)
  print(Fore.GREEN +f"\nEl ordenador adivina: {intento}")
  print("Procesando...")
  time.sleep(2)

  if intento == numero_secreto:
    print("\nEl ordenador ha adivinado el numero."+"\n")
    return True
  
  elif intento < numero_secreto:
    print("\nEl numero secreto es mayor.")

  else:
    print("\nEl numero secreto es menor.") 

    return False 
 
  