# Leibniz Formula
def leibniz(terms):
    total = 0

    for i in range(terms):
        leibniz = (-1)**i/(2*i+1)
        total += leibniz

    # Since Leibniz formula is pi/4 , we have to multiply by 4 to get Pi
    piApprox = 4*total

    return piApprox

