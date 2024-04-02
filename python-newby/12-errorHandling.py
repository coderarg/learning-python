# Error Handling

numberOne, numberTwo = 5, 1

numberTwo = "1"

""" We can prevent an error with an "if- else" condition, 
but if we do not know when the error might appear, ..."""

if type(numberOne) == int and type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("Both numbers must to be integers")

"""...we must use a "try-except" condition to handle the error properly."""

try:
    print(numberOne + numberTwo)
except:
    print("It doesn't work")


numberOne, numberTwo = 5, 1
## next step
try: #(required)
    print(numberOne + numberTwo)
except: #(required)
    print("It doesn't work")
else: # (optional) Else runs if the "try" condition runs
    print("The execution continue correctly")
finally: # (optional)"Finally" sentence always runs at the end
    print("The execution ends")

# We can add type of error conditions in several "except" clause
numberOne, stringNumber = 5, "1"
try:
    print(numberOne + stringNumber)
except TypeError: # Only handle "TypeError" errors
    print("Error: Type Error")
except ValueError: # Only handle "ValueError" errors
    print("Error: Value Error")

# Inform the type of error
try:
    print(numberOne + stringNumber)
    print("All right")
except ValueError as error:
    print(error)
except Exception as exceptionError:
    print(exceptionError)

