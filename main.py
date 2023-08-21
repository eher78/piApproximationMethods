# The entire interface for calculating/approximating pi.

from monteCarlo import monteCarlo
from leibniz import leibniz
from ramanujanSato import ramanujanSato
from riemannSum import riemann

from math import pi

def main():
    print("Please select a method to approximate Pi.")
    print("1. Monte Carlo")
    print("2. Leibniz")
    print("3. Ramanujan Sato")
    print("4. Riemann")
    print("5. All Functions")
    print("6. Pi Actual Value")
    print("7. Quit Program")
    choice = int(input("\nPlease select a number: "))

    if choice == 1:
        monteCarloSimulation()
    elif choice == 2:
        leibnizSimulation()

def monteCarloSimulation():
    option = False

    while option == False:
        simulationNumber = int(input("Type in the number of observations for this method: "))
        piApprox = monteCarlo(simulationNumber)

        print(f"The actual value of pi is: {pi}")
        print(f"The Monte Carlo method is: {piApprox}")

        again = input("Would you like to try again? Y/N ")
        again = again.lower()

        if again == "y":
            option = False
        else:
            option = True
            main()

def leibnizSimulation():
    option = False

    while option == False:
        terms = int(input("Type in the number of terms for this method: "))
        piApprox = leibniz(terms)

        print(f"The actual value of pi is: {pi}")
        print(f"The Leibniz Series method is: {piApprox}")

        again = input("Would you like to try again? Y/N ")
        again = again.lower()

        if again == "y":
            option = False
        else:
            option = True
            main()


main()
