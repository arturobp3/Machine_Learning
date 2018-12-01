import matplotlib.pyplot as plt
from Pract0Iterativo import integra_mc as it
from Pract0Vectores import integra_mc as vec
import numpy as np

def main(a, b, fun):
    ptsIt = []
    ptsVec = []
    
    for i in range(0, 7):
        ptsIt += [it(fun, a, b, 10**i)[1]]
        ptsVec += [vec(fun, a, b, 10**i)[1]]

    plt.figure()
    plt.scatter(range(0,7), ptsIt, c='red', label='iterativo')
    plt.scatter(range(0,7), ptsVec, c='blue', label='vectorizado')
    plt.legend()
    
    
        
a = 0
b = np.math.pi
fun = lambda x: x**2

main(a,b,fun)