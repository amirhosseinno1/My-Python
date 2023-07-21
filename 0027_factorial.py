def fact(i):
    'calculate factorial'
    fact = 1
    j = 1
    while j <= i :
        fact *= j
        j += 1
    return fact
x = int(input('x : '))
print(fact(x))

import math as mt
y = int(input('y : '))
print (mt.factorial(y))
