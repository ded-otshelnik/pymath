from copy import copy
from .transpose import transpose
from .matrix_iter import MatrixIter
from typing import Iterable

class Matrix(Iterable):
    """
    Class represents 2-d matrix and operations related to matrixes.
    """
    def __init__(self, matrix):
        # TODO: add error throwing and check
        self._matrix = matrix
        self._shape = (len(matrix),len(matrix[0]))
        
    def __eq__(self, other_matrix):
        # TODO: add error throwing and check
        for value1,value2 in zip(self,other_matrix):
            if value1 != value2:
                return False
        return True

    def __repr__(self):
        return f"Matrix({str(self)})"
    
    def __str__(self):
        _str = "["
        for index in range(len(self._matrix)):
            _str += str(self._matrix[index]) + (",\n" if index < len(self._matrix) - 1 else "")
        _str += "]"
        return _str
    
    def __len__(self):
        return len(self._matrix)
    
    def __add__(self,other_matrix):
        return self.add(other_matrix)
    
    def __mul__(self,other_matrix):
        return self.dot(other_matrix)
    
    def __getitem__(self,index):
        return self._matrix[index]
    
    @property
    def shape(self):
        return copy(self._shape)
    @property 
    def T(self):
        return Matrix(transpose(self._matrix))

    def add(self,other_matrix):
        # TODO: add error throwing and check
        result = []
        # loop by rows of two matrixes
        for row1, row2 in zip(self,other_matrix):
            result.append([])
            # loop by items of two rows
            for item1, item2 in zip(row1,row2):
                # add sum of items
                result[len(result)-1].append(item1 + item2)
        return Matrix(result)
    
    def dot(self,other_matrix):
        # TODO: add error throwing and check
        result = []
        for row in self:
            result.append([])
            # loop by columns of B
            for column in other_matrix.T:
                # append product of current column and row
                result[len(result)-1].append(sum([a*b for a,b in zip(row,column)]))  
        return Matrix(result)

    def __iter__(self):
        return MatrixIter(self)
    
if __name__ == "__main__":
    matrix = Matrix([[1,2],[3,4]])
    print(matrix)
    print(matrix.T)
    print(matrix[0])
    print(matrix.shape)
    for i in matrix:
        print(i)

    matrix2 = Matrix([[1,2]])
    print(matrix2.shape)
    print(matrix2.T)

    matrix3 = Matrix([[1,2],[3,4]])
    print(matrix == matrix3)

    print(matrix.__repr__())

    print(matrix.add(matrix3))
    print(matrix.dot(matrix3))