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

def transpose(A:list[list])->list[list]:
    """
    Function returns a transposed matrix

    Args:
        A (list[list]): matrix

    Returns:
        list[list]: transposed matrix
    """

    return list(list(row) for row in zip(*A))


def dot(A:list[list[float]] | list[list[int]], B:list[list[float]] | list[list[int]]) -> list[list[float]] | list[list[int]]:
    """
    Function computes product of two matrixes.    

    Args:
        A (list[list[float]] | list[list[int]]): first matrix 
        
        B (list[list[float]] | list[list[int]]): second matrix

    Raises:
        ValueError: if dimentions are not aligned
        TypeError: if types are unsupposed for + or *

    Returns:
        list[list[float]] | list[list[int]]: product of matrix multiplying
    """

    # checking block

    # checking for not empty matrixes
    check_not_empty_A = False in [len(row)!= 0 for row in A]
    check_not_empty_B = False in [len(row)!= 0 for row in B]
    
    if check_not_empty_A or check_not_empty_B or len(A) == 0 or len(B) == 0:
        raise ValueError("matrixes mustn't be empty.")
    
    # checking dimentions and align

    check_dim_A = False in [len(A[i])==len(A[i-1]) for i in range(1,len(A))]
    check_dim_B = False in [len(B[i])==len(B[i-1]) for i in range(1,len(B))]

    if check_dim_A or check_dim_B or len(A[0]) != len(B):
        raise ValueError("shapes not aligned: " + 
                         "("+str(len(A))+"," + (str(len(A[0])) if check_dim_A else "") + ") and ("+
                         (str(len(B[0])) if check_dim_B else "") + ","+ str(len(B[0]))+")")
    
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
    return result