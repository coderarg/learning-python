# Challenges
# from https://retosdeprogramacion.com/ejercicios/


"""
* Escribe un programa que muestre por consola (con un print) los
* números de 1 a 100 (ambos incluidos y con un salto de línea entre
* cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

fizzbuzz_array = []
fizzbuzz_string = ""

for i in range(1, 100):
    if(i%3 == 0 and i%5 ==0):
        fizzbuzz_array.append("fizzbuzz")
    elif(i%3 == 0 and i%5 != 0):
        fizzbuzz_array.append("fizz")
    elif(i%3 != 0 and i%5 == 0):
        fizzbuzz_array.append("buzz")
    else: 
        fizzbuzz_array.append(i)

for elem in fizzbuzz_array:
    fizzbuzz_string = fizzbuzz_string + "\n" + str(elem)

# print(fizzbuzz_string.strip())

# Mejora de fizzbuzz
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index %3 == 0:
            print("fizz")
        elif index %5 == 0:
            print("buzz")
        else:
            print(index)

#fizzbuzz()

"""
* Escribe una función que reciba dos palabras (String) y retorne
* verdadero o falso (Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
"""
def is_anagrama(word_1: str, word_2: str):
    if word_1.lower() == word_2.lower():
        return False
    print(sorted(word_1.lower()) == sorted(word_2.lower()))

#is_anagrama("Amor", "Roma")


""" 
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
*   0, 1, 1, 2, 3, 5, 8, 13...
"""



def fibonacci_serie(iterations):
    
    before_previous = 0
    previous = 1
    fibonacci_sequence = [0, 1]

    for it in range(2, iterations, 1):
        actual_number = before_previous + previous
        before_previous = previous
        previous = actual_number
        fibonacci_sequence.append(actual_number)
        
    print(fibonacci_sequence)

fibonacci_serie(6)

""" 
* Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
"""

def generate_prime_numbers():

    prime_numbers = []
    
    for index_a in range(3, 100):
        isPrime = True

        for index_b in range(2, index_a):
          if index_b != index_a:
            if index_a % index_b == 0:
                isPrime = False
        
        if isPrime:
            prime_numbers.append(index_a)
            
    print(prime_numbers)

#generate_prime_numbers()

""" 
* Crea un programa que invierta el orden de una cadena de texto
* sin usar funciones propias del lenguaje que lo hagan de forma automática.
* Si le pasamos "Hola mundo" nos retornaría "odnum aloH" 
"""

def reverse_string(characters):

    reversed_string = ''
    string_length = len(characters)

    for index_letter in range(0, string_length):
        reversed_string += characters[string_length - index_letter - 1]
    
    print(reversed_string)


reverse_string("Buenas tardes, que onda, todo piola?")
    