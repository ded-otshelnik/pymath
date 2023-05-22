from typing import Iterator

class MatrixIter(Iterator):
    """
    Class implements an iterator for Matrix class.
    Iterate by row each element.
    """
    def __init__(self,matrix) -> None:
        self._matrix = matrix._matrix
        self._rows, _ = matrix._shape
        self._current_row = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self._current_row < self._rows:
            self._current_row += 1 
            return self._matrix[self._current_row-1]
        raise StopIteration