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