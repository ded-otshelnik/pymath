def transpose(matrix):
    """
    Function returns a transposed matrix.

    Args:
        matrix: MatrixLike, matrix.

    Returns:
        MatrixLike: transposed matrix.
    """

    return list(list(row) for row in zip(*matrix))

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    print(transpose(A))
    import numpy as np
    print(np.transpose(A))