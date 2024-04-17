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
    return sorted(word_1.lower()) == sorted(word_2.lower())

print(is_anagrama("Amor", "Roma"))


""" 
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 """

""" def fibonacci_serie(iterations):
    previous = 0
    next = 1
    for it in range(0, iterations, 1):
        
 """