import unittest
from unittest.mock import patch
from jugador import turno_jugador
from logica_juego import generar_numero_secreto

class TestLogicaJuego(unittest.TestCase):

    def test_generar_numero_secreto(self):
        numero = generar_numero_secreto()
        self.assertTrue(1 <= numero <= 100)


class TestJugador(unittest.TestCase):
    
    @patch('builtins.input')
    def test_turno_jugador(self, mock_input):
        # Simulamos que el jugador ingresa '50'
        mock_input.return_value = '50'
        
        numero_secreto = 50  # Ejemplo de un número secreto
        tentativas_jugador = []  # Lista vacía de tentativas
        
        # Llamamos a la función pasando los argumentos correctos
        resultado = turno_jugador(numero_secreto, tentativas_jugador)
        
        # Comprobamos que el jugador adivinó correctamente
        self.assertTrue(resultado)
        # Comprobamos que el intento se guardó en tentativas_jugador
        self.assertIn(50, tentativas_jugador)


         
    @patch('builtins.input', return_value='105')
    def test_numero_fuera_de_rango(self, mock_input):
        numero_secreto = 50
        tentativas_jugador = []

        resultado = turno_jugador(numero_secreto, tentativas_jugador)

        # Verificar que input fue llamado correctamente
        mock_input.assert_called_once()

        # Comprobar si la función devuelve False cuando el jugador ingresa un número fuera de rango
        self.assertFalse(resultado, "La función debería devolver False para números fuera de rango.")
        # Comprobar que el número fuera de rango NO se añadió a la lista de tentativas
        self.assertNotIn(105, tentativas_jugador,"El número fuera de rango no debería añadirse a la lista de tentativas." )

if __name__ == '__main__':
    unittest.main()