def add(A:list[list[float]] | list[list[int]], B:list[list[float]] | list[list[int]])->list[list]:
    """
    Function computes product of two matrixes.    

    Args:
        A (list[list[float]] | list[list[int]]): first matrix 
        
        B (list[list[float]] | list[list[int]]): second matrix

    Raises:
        ValueError: if dimentions are not aligned
        TypeError: if types are unsupposed for + or *

    Returns:
        list[list]: product of matrix multiplying
    """
    # checking block

    # checking for not empty matrixes
    check_not_empty_A = False in [len(row)!= 0 for row in A]
    check_not_empty_B = False in [len(row)!= 0 for row in B]
    
    if check_not_empty_A or check_not_empty_B or len(A) == len(B) == 0:
        raise ValueError("matrixes mustn't be empty.")
    
    # checking dimentions and align

    check_dim_A = False in [len(A[i])==len(A[i-1]) for i in range(1,len(A))]
    if check_dim_A or len(A) != len(B):
        raise ValueError("uncombatible matrixes: shapes are not equal")

    result = []
    # loop by rows of two matrixes
    for row1, row2 in zip(A,B):
        result.append([])
        # loop by items of two rows
        for item1, item2 in zip(row1,row2):
            # add sum of items
            result[len(result)-1].append(item1 + item2)
    return result

if __name__ == "__main__":
    A = [[1,2,3], [4,5,6]]
    B = [[1,2,3], [4,5,6]]
    print(add(A, B))
    import numpy as np
    print(np.add(A, B))  