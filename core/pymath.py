from typing import Callable
import math

def cos(x:float,n:int)->float:
    '''
        Function computes value of cos(x) as Taylor series,
        returns value with accuracy of n parts of series.

        Necessary keyword arguments:
        x: argument of cos function
        n: value of series parts   
    '''
    result = 1
    curr = 1

    # cos(x) = 1 - (x^2)/(2!) + (x^4)/(4!) + ... + (-1)^n * x^(2*n)/((2*n)!)

    for i in range(1,n):
        curr *= (-1)*(x*x) / (( 2*i - 1 )*(2*i))
        result += curr
    return result

def sqrt(x:float|complex, approx:int = 10)->float|complex:
    '''
    Function computes square root of float or complex number
    
    Necessary keyword arguments:
    x: float|complex: number, what is used for computing the root.
    approx: int,optional: acceptable error for evaluation
    -----
    Return - float value (if x>=0) or complex value(if x<0)
    '''
    if isinstance(x,complex):
        # if we can compute as sqrt of float
        if x.imag == 0:
            #recursively call sqrt of real part 
            result = sqrt(x.real) 
        else:
            a, b = x.real, x.imag
            # sqrt(z) = sqrt((|z| + a)/2) + (b/|b|) * sqrt((|z| - a)/2) * i
            real = sqrt((sqrt(a**2 + b**2) + x.real)/2)
            imag = b/(-b if b < 0 else b) * sqrt((sqrt(a**2 + b**2) + x.real)/2)
            result = complex(real=real,imag=imag)
    # if float value is less than zero
    elif x < 0:
        number = complex(0,x)
        # recursively call sqrt of complex number with zero real part
        result = sqrt(number)
    else:
        # method of half division
        result = x/2
        t = 0
        comp = t - result
        while (comp if comp>0 else -comp) > 10**(-approx) :
            t = result
            # Geron's formula 
            # x_(n+1) = (x_n + a/x_n), lim x_n = sqrt(a) 
            result = (t + (x/t))/2
            comp = t - result
    return result

LEFT_RECT = "l"
RIGHT_RECT = "r"
CENTER_RECT = "c"

def rect_integral(f:Callable[[float], float], a:float, b:float, n:int, method:str = "l")->float:
    '''
    Computes integral of function f on an interval from a(includive) to b(includive)
    with number of splits n using rectangle method. 

    Necessary keyword arguments:
    f: Callable[[float], float] - function
    a: float - left border of interval
    b: float - right border of interval
    n: int - number of splits
    method: str - keyword for choosing method of integration, 'l' - left rectangle, 'r' - right rectangles,
    'c' - center rectangles. If value not 'l','r' or 'c' exception will be occured.
    '''
    result = 0

    # step of integration
    h = (b - a) / n

    # integral = (f(value_1) + f(value_2) + ... + f(value_n)) * h 
    # values depend on type of rectangles method
    # left: a + i * h
    # right: a + (i + 1) * h
    # center: (a + i * h + a + (i + 1) * h) / 2

    for i in range(0,n):
        # if we use left rectangles
        if method == LEFT_RECT:
            value = a + i * h
        # if we use right rectangles
        elif method == RIGHT_RECT:
            value = a + (i + 1) * h
        # if we use center rectangles
        elif method == CENTER_RECT:
            value = (a + i * h + a + (i + 1) * h) / 2
        # if incorrect argument of method
        else:
            raise ValueError("incorrect argument of integration method")
        
        result += f(value) 
    
    return result * h

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
        raise ValueError(f"Imcopatible length: {len(x)} != {len(y)}")
    if len(x) == 0:
        raise ValueError("Lists mustn't be empty.")
    for item in x:
        if not isinstance(item, float):
            raise TypeError("Arguments must be float.")

    # Newton polynomial is a sum of values a_i * w
    # where w is a product of (x - x[i-1]) 
    # and a_k is coefficient
    from sympy import symbols, Poly, factorial
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
    return Poly(temp,X)

def lagrange(x:list,y:list[float]):
    '''
    Computes lagrange polynomial of function that is defined as lists of arguments and values.

    Necessary keyword arguments:
    x0 : list - arguments
    y : list[float] - values
    -----
    Return - an Poly object (defined in sympy module) 
    '''
    # Check before running
    if len(x) != len(y):
        raise ValueError(f"Imcopatible length: {len(x)} != {len(y)}")
    if len(x) == 0:
        raise ValueError("Lists mustn't be empty.")
    for item in x:
        if not isinstance(item, float):
            raise ValueError("Arguments must be float.")

    from sympy import symbols, Poly
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

def linspace(start:float,stop:float,num:int)->list:
    '''
    Return evenly spaced numbers over a specified interval.
    
    Returns num evenly spaced samples, calculated over the interval [start, stop].
    '''    
    # check values of start and stop for calculating step
    reverse_cond = stop - start < 0
    # if we stop less than step
    if reverse_cond:
        # exchange start and stop
        stop, start = start, stop

    # step of generation 
    h = (stop - start) / (num - 1)
    # result list
    result = [start, stop]
    
    # add values in result list
    i = 1
    while True:
        if(start + i*h >= stop):
            break
        result.insert(i,start + i*h)
        i+=1

    # if we exchanged start and stop
    if reverse_cond:
        # reverse result list
        result.reverse()
    return result