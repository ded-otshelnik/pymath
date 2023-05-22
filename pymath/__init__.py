"""
pymath
-----
This module provides:
1. Interpolation polynomials (Lagrange,Newton)
2. Some functions (cos, sqrt)
3. Integrate by rectangle method
4. Matrixes

Submodules
----
matrix - provide matrixes and related operations

Functions
----
cos - cos by Taylor series
lagrange - interpolation polynomial by Lagrange
newton - interpolation polynomial by Newton
rect_integral - integrate by rectangle method
linspace - evenly spaced numbers over a specified interval
"""

from pymath.lagrange import lagrange
from pymath.linspace import linspace
from pymath.newton import newton
from pymath.rect_integral import rect_integral,LEFT_RECT,RIGHT_RECT,CENTER_RECT
from pymath.sqrt import sqrt
from pymath.cos import cos

from pymath import matrix