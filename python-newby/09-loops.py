# Loops

## Comprobar si números son pares o impares
for i in range(1, 21):
    if i % 2 == 0:
        print('El número ',i, ' es par')
    else:
        print('El número ',i, ' es impar')

# El mismo ejemplo anterior, pero resuelto con un ciclo while
# resuelto con while

i = 1
while (i <= 20):
    if (i % 2 == 0):
        print('El numero' ,i, 'es par')
    else:
        print('El numero' ,i, 'es impar')
    i = i + 1

# break en ciclo for

cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        # print("Se encontró la h")
        break
    # print(letra)

# break en ciclo while

x = 5
while x > 0:
    x -= 1 # x = x - 1
    # print(x)
    if x == 0:
        break
# print("Fin del bucle")

# continue
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    # print(letra)


# For loop with Else condition
email = "lucasgarcia@tuemail.com"

for letter in email:
    print(letter)
else:
    print("The loop finished")
# the else condition is executed when the loop finished 
# but only in the case that all the iterations was executed successfully
# if the loop were broken by an error, the else condition wouldn't be executed

