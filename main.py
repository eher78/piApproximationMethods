# The entire interface for calculating/approximating pi.

from monteCarlo import monteCarlo
from leibniz import leibniz
from ramanujanSato import ramanujanSato
from riemannSum import riemann


print("This is a Pi approximation calculator. Please select the type of approximation you would like to use.")
while True:
    print("1. Monte Carlo")
    print("2. Leibniz")
    print("3. Ramanujan Sato")
    print("4. Riemann")
    print("5. All Functions")
    print("6. Pi Actual Value")
    print("7. Quit Program")
    choice = int(input("\nPlease select a number: "))

    if choice == 1:
        print("Selecting Monte Carlo...")

