from sympy import symbols, Poly

import numpy as np
import matplotlib.pyplot as plt

def lagrange(x:list,y:list[float]) -> Poly:
    '''
    lagrange(x:list,y:list[float]) -> Poly

    Computes lagrange polynomial of function that is defined as lists of arguments and values.

    Necessary keyword arguments:
    x0 : list - arguments
    y : list[float] - values
    -----
    Return - an Poly object (defined in sympy module) 
    '''

    # Check before running
    assert len(x) == len(y), f"Imcopatible length: {len(x)} != {len(y)}"
    assert len(x) != 0, "Lists mustn't be empty."
    for item in x:
        assert isinstance(item, float), "Arguments must be float."

    # Parametrization of variable
    _x = symbols('x')

    # lagrange polynomial is sum (by i) of elements of y[i] * (x - x0[j])/(x0[i] - x0[j])), i != j

    temp = 0
    for i in range(len(y)):
        nominator = 1
        denominator = 1
        for j in range(len(x)):
             if i != j:
                 nominator *= _x - x[j]
                 denominator *= (x[i] - x[j])
        temp += y[i] * nominator/denominator

    # Return polynomial with x variable
    return Poly(temp, x)

if __name__ == "__main__":
    f = lambda x: np.sin(x)
    x = np.linspace(-2, 2, 10)
    y = f(x)

    poly = lagrange(x.tolist(), y)

    x = np.linspace(-3, 3, 1000)
    y = f(x)

    y_eval = [poly(i) for i in x]
    plt.plot(x, y_eval)
    plt.plot(x, y)
    plt.show()
