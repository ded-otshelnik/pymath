from sys import exit

def sqrt(x:float|complex, approx:int = 10)->float|complex:
    '''
    sqrt(x:float|complex, approx:int = 10)->float|complex
    
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
    
if __name__ == "__main__":
    ch = 0
    input_string = "Enter the type of number:\n1. Float\n2. Complex\n3. Exit\nYour choice: "
    correct_input = False
    while not correct_input:
        ch = input(input_string)
        try:
            ch = int(ch)
        except ValueError:
            print("Incorrect choice. Please try again.",sep="\n\n")
            continue
        while not ch in [1,2,3]:
            print("Choice must be 1 or 2. Please try again.",sep="\n\n")
            continue
        correct_input = True
    correct_input = False
    approx = 2
    while not correct_input:
        temp = input("Enter approximation: ")
        try:
            approx = int(temp)
        except ValueError:
            print("Incorrect input. Please try again.",sep="\n\n")
            continue
        correct_input = True
    if ch != 3:
        correct_input = False
        number = 0 
        while not correct_input:
            if ch == 1:
                temp = input("Enter the number (e.g. 1.0): ")
                try:
                    number = float(temp)
                except ValueError:
                    print("Incorrect input. Please try again.",sep="\n\n")
                    continue
                correct_input = True
            elif ch == 2:
                real = input("Enter the the real part of number (e.g. 1.0): ")
                try:
                    real = float(real)
                except ValueError:
                    print("Incorrect input. Please try again.",sep="\n\n")
                    continue
                imag = input("Enter the the imag part of number (e.g. 1.0): ")
                try:
                    imag = float(imag)
                except ValueError:
                    print("Incorrect input. Please try again.",sep="\n\n")
                    continue
                number = complex(real,imag)
                correct_input = True
        result = sqrt(number)
        print("Square root of ",end="")
        if isinstance(number,complex):
            print(str(round(number.real,approx)) + "+"+str(round(number.imag,approx)) + "i",end="")
        else:
            print(number,end="")
        print(" is ",end="")
        if isinstance(result,complex):
            print("\u00b1("+ str(round(result.real,approx)) + "+" + str(round(result.imag,approx)) + "i)")
        else:
            print(result,end="")
    else:
        exit()