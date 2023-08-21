from decimal import Decimal
from math import pi, sqrt, factorial

def ramanujanSato(terms):
    # Limit of Terms is 129!
    pi = Decimal(pi)
    terms = 100
    sum = 0

    constant = Decimal((2*sqrt(2))/(99**2))

    for i in range(terms):
        factorialPart = Decimal((factorial(4*(i)))/((factorial(i))**4))
        otherPart = Decimal(((26390*i)+1103)/(396**(4*i)))
        sum += Decimal((factorialPart * otherPart))

    total = Decimal(constant * sum)

    piApprox = Decimal(1/(total))

    return piApprox
