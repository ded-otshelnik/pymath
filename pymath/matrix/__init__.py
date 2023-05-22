"""
pymath.matrix
-----
This module provides matrixes and some related operations like transpose, add or dot.

Classes
----
Matrix - class represents matrixes

Functions
----
add - sum of two matrixes

dot - product of two matrixes

transpose - matrix transposing
"""

from pymath.matrix.add import add
from pymath.matrix.transpose import transpose
from pymath.matrix.dot import dot
from pymath.matrix.matrix import Matrix

from pymath.matrix.matrix_typing import scalar,MatrixLike