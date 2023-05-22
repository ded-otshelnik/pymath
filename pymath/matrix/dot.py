from .transpose import transpose
from .matrix import Matrix

from typing import TypeAlias

scalar: TypeAlias = int | float | complex
MatrixLike: TypeAlias = list[list[scalar]]

def dot(A, B):
    """
    Function computes product of two matrixes.    
    
    Args:
        A: Matrix: first matrix 
        
        B: Matrix: second matrix

    Raises:
        ValueError: if dimentions are not aligned
        TypeError: if types are unsupposed for + or *

    Returns:
        Matrix: product of matrix multiplying
    """
    # checking block

    if not isinstance(A,Matrix) or not isinstance(B,Matrix):
        raise ValueError("Arguments must be matrixes")
    for row1,row2 in zip(A,B):
        for val1,val2 in zip(row1,row2):
            if not isinstance(val1,scalar) or not isinstance(val1,scalar):
                raise TypeError("Values of matrixes must be scalar")

    # transposing B matrix before multiplying 
    B = transpose(B)
    result = []

    # loop by rows of A
    for row in A:
        result.append([])
        # loop by columns of B
        for column in B:
            # append product of current column and row
            result[len(result)-1].append(sum([a*b for a,b in zip(row,column)]))  
    return Matrix(result)

if __name__ == "__main__":
    A = Matrix([[1,2,3],[4,5,6]])
    B = Matrix([[1],[2],[3]])
    print(dot(A,B))
    print(A.dot(B))
    import numpy as np
    print(np.dot(A,B))