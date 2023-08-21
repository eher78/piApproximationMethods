import numpy as np

def riemann(N):
    f = lambda x: np.sqrt(1 - x**2)
    a = -1
    b = 1
    N = 100000000

    dx = (b - a) / N
    x_midpoint = np.linspace(a + dx / 2, b - dx / 2, N)

    midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)

    piApprox = midpoint_riemann_sum * 2
    return piApprox