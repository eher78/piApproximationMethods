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
    elif choice == 3:
        ramanujanSimulation()
    elif choice == 4:
        riemannSimulation()
    elif choice == 5:
        allSimulations()
    elif choice == 6:
        piValue()
    elif choice == 7:
        return
    else:
        print("Not a valid value. Please try again.")
        main()




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

def ramanujanSimulation():
    option = False

    while option == False:
        terms = int(input("Type in the number of terms for this method: "))
        piApprox = ramanujanSato(terms)

        print(f"The actual value of pi is: {pi}")
        print(f"The Ramanujan-Sato Series method is: {piApprox}")

        again = input("Would you like to try again? Y/N ")
        again = again.lower()

        if again == "y":
            option = False
        else:
            option = True
            main()


def riemannSimulation():
    option = False

    while option == False:
        terms = int(input("Type in the number of terms for this method: "))
        piApprox = riemann(terms)

        print(f"The actual value of pi is: {pi}")
        print(f"The Riemann Approximation method is: {piApprox}")

        again = input("Would you like to try again? Y/N ")
        again = again.lower()

        if again == "y":
            option = False
        else:
            option = True
            main()

def allSimulations():
    option = False

    while option == False:
        terms = int(input("Type in the number of values for all methods: "))
        monteCarloApprox = monteCarlo(terms)
        leibnizApprox = leibniz(terms)
        ramanujanSatoApprox = ramanujanSato(terms)
        riemannApprox = riemann(terms)

        print(f"The actual value of pi is: {pi}")
        print(f"The Monte Carlo Approximation is: {monteCarloApprox}")
        print(f"The Leibniz Approximation is: {leibnizApprox}")
        print(f"The Ramanujan Sato Approximation is: {ramanujanSatoApprox}")
        print(f"The Riemann Approximation is: {riemannApprox}")


        again = input("Would you like to try again? Y/N ")
        again = again.lower()

        if again == "y":
            option = False
        else:
            option = True
            main()

def piValue():
    option = False
    while option == False:
        print(f"The actual value of pi is: {pi}")
        again = input("Would you like to try again? Y/N ")
        again = again.lower()

        if again == "y":
            option = False
        else:
            option = True
            main()


main()
