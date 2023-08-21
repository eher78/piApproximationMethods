import numpy as np

def monteCarlo(trials):

    r = 1

    nInside = 0

    xPoints = []
    yPoints = []

    for i in range(trials):
        x_random = np.random.uniform(-1, 1, 1)
        y_random = np.random.uniform(-1, 1, 1)

        xPoints.append(x_random)
        yPoints.append(y_random)

    for i in range(trials):
        x = xPoints[i]
        y = yPoints[i]

        if x**2 + y**2 < r**2:
            nInside += 1
        

    piApprox = 4*nInside/trials
    return piApprox
