# Modules
# File which calls other file function

import module
module.multiply_two_values(2, 3)
module.printValue("Hello module!")

from module import multiply_two_values, printValue
multiply_two_values(2, 3)
printValue("Hello module!")

#We can use Python system modules
import math
print(math.pi)

from math import pi as PI_VALUE
print(PI_VALUE)