def transpose(A:list[list])->list[list]:
    """
    Function returns a transposed matrix

    Args:
        A (list[list]): matrix

    Returns:
        list[list]: transposed matrix
    """

    return list(list(row) for row in zip(*A))

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    print(transpose(A))
    import numpy as np
    print(np.transpose(A))