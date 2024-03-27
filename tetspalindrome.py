import unittest
"""
def obtener_cantidad_de_palabras_palindrome(lista):
    contador = 0
    for palabra in lista:
        palindromo = 0
        if len(palabra) % 2 == 0 :
            for valor in range(len(palabra)):
                reversa = -(valor+1)
                if palabra[valor] == palabra[reversa]:
                    palindromo += palindromo
                    if len(palabra)/2 == palindromo:
                        contador+=contador
                else:
                    continue
        else:
            for valor in range(len(palabra)):
                reversa = -(valor+1)
                if palabra[valor] == palabra[reversa]:
                    palindromo += palindromo
                    if (len(palabra)-1)/2 == palindromo:
                        contador+=contador
                else:
                    continue
    return contador
"""

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    for valor in range(len(palabra)):
        reversa = -(valor+1)
        if palabra[valor]!=palabra[reversa]:
            return False
    return True

def obtener_cantidad_de_palabras_palindrome(lista):
    contador = 0
    for palabra in lista:
        if es_palindromo(palabra):
            contador = contador +1
    return contador


class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        lista = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        lista = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        lista = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        lista = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        lista = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 3)



    def test_cantidad_de_palabras_palindromes_complejo(self):
        lista = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        lista = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 5) 


unittest.main()
