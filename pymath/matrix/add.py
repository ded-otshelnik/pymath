from .matrix import Matrix

from typing import TypeAlias

scalar: TypeAlias = int | float | complex
MatrixLike: TypeAlias = list[list[scalar]]

def add(A, B):
    """
    Function computes product of two matrixes.    

    Args:
        A Matrix: first matrix 
        
        B Matrix: second matrix

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

    result = []
    # loop by rows of two matrixes
    for row1, row2 in zip(A,B):
        result.append([])
        # loop by items of two rows
        for item1, item2 in zip(row1,row2):
            # add sum of items
            result[len(result)-1].append(item1 + item2)
    return Matrix(result)

if __name__ == "__main__":
    A = Matrix([[1,2,3], [4,5,6]])
    B = Matrix([[1,2,3], [4,5,6]])
    print(add(A, B))
    import numpy as np
    print(np.add(A, B))  