# Pi Approximation Methods

This repository explores various mathematical techniques to approximate the value of the mathematical constant π (pi). The methods implemented in this project include the Leibniz Series, Ramanujan-Sato Series, Monte Carlo simulation, and Riemann Sum. These methods showcase different approaches to estimating π and a brief guide to how it works.

## Methods Explored

### 1. Leibniz Series
The Leibniz Series, attributed to the mathematician Gottfried Wilhelm Leibniz, is an infinite series that converges to π/4. The formula is derived from the Maclaurin series of the arctangent function. 

### 2. Ramanujan-Sato Series
The Ramanujan-Sato Series is based on the work of the legendary mathematician Srinivasa Ramanujan. This formula converges to many digits of π with just a few terms. 

### 3. Monte Carlo Simulation
Monte Carlo simulation is a statistical technique that uses random sampling to obtain numerical results. In the context of approximating π, a Monte Carlo simulation involves generating random points within a square and determining the ratio of points that fall within a quarter circle inscribed within the square. 

### 4. Riemann Sum
The Riemann Sum is a method from calculus that approximates the area under a curve by dividing it into smaller segments. In the context of calculating π, you can use the Riemann Sum to estimate the area under the curve of the quarter circle. As the number of divisions increases, the approximation becomes more accurate.

## Getting Started
To explore the various π approximation methods implemented in this repository, follow these steps:

1. The interface will tell the user to select an integer based on a method to approximate Pi.
2. The user selects the method to choose which includes the four methods listed above or using all methods or finding the actual pi value.
3. For each method used, there will be a prompt to put in an integer-based value for the number of terms or values for that method. We would recommend to keep the values below 100 for computational and memory allocation.
4. Should you wish to end the program, feel free to type in "n" or 7 depending on the prompt.
