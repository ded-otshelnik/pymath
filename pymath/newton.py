import math
import numpy as np
from sympy import symbols, Poly, factorial

import matplotlib.pyplot as plt

from pymath.matrix.matrix_typing import scalar

def newton(x:list,y:list[float]):
    '''
    Computes newton polynomial of function that is defined as lists of arguments and values.

    Necessary keyword arguments:
    x : list - arguments
    y : list[float] - values
    -----
    Return - an Poly object (defined in sympy module) 
    '''

    # Check before running
    if len(x) != len(y):
        raise ValueError(f"Imcompatible length: {len(x)} != {len(y)}")
    if len(x) == 0:
        raise ValueError("Lists mustn't be empty.")
    for item in x:
        if not isinstance(item, scalar):
            raise TypeError("Arguments must be float.")

    # Newton polynomial is a sum of values a_i * w
    # where w is a product of (x - x[i-1]) 
    # and a_k is coefficient

    # binomial coefficients for a_i computing 
    def c_coeff(i):
        c = []
        for k in range(0, i+1):
            c.append(math.comb(i,k))
        return c
    

    X = symbols('x')
    temp = y[0]
    # step of computing
    h = x[1] - x[0]
    w = 1
    for i in range(1,len(y)):
        a = 0
        c = c_coeff(i)
        for k in range(0, i+1):
            a += c[k] * (-1)**k * y[i-k]
            if k == i:
                a /= factorial(k) * h**k
        w *= X - x[i-1]
        temp += a*w

    # Return polynomial with x variable
    return Poly(temp)

if __name__ == "__main__":
    f = lambda x: np.sin(x)
    x = np.linspace(-2, 2, 10)
    y = f(x)

    poly = newton(x.tolist(), y)

    x = np.linspace(-3, 3, 1000)
    y = f(x)

    y_eval = [poly(i) for i in x]
    plt.plot(x, y_eval)
    plt.plot(x, y)
    plt.show()
