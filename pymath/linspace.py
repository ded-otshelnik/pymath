import numpy as np

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

if __name__ == "__main__":
    n1 = linspace(0,2.086,21)
    n2 = linspace(2.086,0,21)
    print(n1)
    print(n2)
    print(len(n1))
    print(len(n2))
    n2.reverse()
    for i,j in zip(n1,n2):
        print(i == j)