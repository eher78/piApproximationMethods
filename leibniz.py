def leibniz(terms):

    total = 0

    for i in range(terms):
        leibniz = (-1)**i/(2*i+1)
        total += leibniz


    piApprox = 4*total

    return piApprox

