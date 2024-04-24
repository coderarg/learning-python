# Lambdas
# Anonymous functions
# It's a function that we execute one time.

estudiantes = [
    ("José", 2),
    ("Pablo", 4),
    ("Marta",1)
]

def retornar_nota(estudiante):
    return estudiante[1]
# We could translate the def function to the next lambda function
lambda x: x[1]

lista_ordenada = sorted(estudiantes, key=lambda x: x[1], reverse=False)
#print(lista_ordenada)