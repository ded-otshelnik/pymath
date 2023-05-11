# 3.1 Taylor series of cos(x)
import numpy as np

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

if __name__ == "__main__":
    start = float(input("Enter start = "))
    stop = float(input("Enter stop = "))
    step = 0.1
    n = int(input("Enter n = "))

    dict_result = {}
    for x in np.arange(start,stop,step):
        dict_result[x] = cos(x,n)

    for key,value in dict_result.items():
        print("{:0.3f} -> {:0.3f}".format(key,value))