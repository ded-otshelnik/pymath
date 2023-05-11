from math import sin
from typing import Callable

LEFT_RECT = "l"
RIGHT_RECT = "r"
CENTER_RECT = "c"

def rect_integral(f:Callable[[float], float], a:float, b:float, n:int, method:str = "l")->float:
    '''
    rect_integral(f:Callable[[float], float], a:float, b:float, n:int, method = LEFT_RECT)->float

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
            raise ValueError
        
        result += f(value) 
    
    return result * h

if __name__ == "__main__":
    f = lambda x: sin(x) 
    print("Function that used in test is sin(x).",sep="\n\n")
    correct_input = False
    a = None
    while not correct_input:
        try:
            a = float(input("Enter left border of an interval(a): "))
        except ValueError:
            print("Incorrect input. Please try again.",sep="\n\n")
            continue    
        correct_input = True

    assert isinstance(a,float)

    correct_input = False
    b = None
    while not correct_input:
        try:
            b = float(input("Enter right border of an interval(b): "))
            assert b >= a
        except ValueError | AssertionError:
            print("Incorrect input. Please try again.",sep="\n\n")
            continue
        correct_input = True

    assert isinstance(b,float)

    correct_input = False
    n = None
    while not correct_input:
        try:
            n = int(input("Enter number of splits: "))
            assert n > 0, "n must be more than 0"
        except AssertionError as e:
            print()
        except ValueError:
            print("Incorrect input. Please try again.",sep="\n\n")
            continue
        correct_input = True
    
    assert isinstance(n,int)

    correct_input = False
    ch = None
    while not correct_input:
        ch = input("Choose method:\n1. Left rectangles\n2. Right rectangles"
                   + "\n3. Center rectangles\nYour choice: ")
        try:
            ch = int(ch)
            assert ch in [1,2,3], "Choice must be 1 or 2. Please try again.\n"
        except ValueError | AssertionError:
            print("Incorrect choice. Please try again.",sep="\n\n")
            continue
        correct_input = True

    assert isinstance(ch, int)

    if ch == 1:
        method = LEFT_RECT
    elif ch == 2:
        method = RIGHT_RECT
    else:
        method = CENTER_RECT
    result = rect_integral(f,a,b,n,method)
    print(f"Result of integration is {result:0.5}.")