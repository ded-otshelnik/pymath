from collections.abc import Iterable

from typing import Iterator, TypeAlias,TypeVar

scalar = TypeVar("scalar",int | float | complex)
MatrixLike: TypeAlias = list[list[scalar]]

class Matrix(Iterable):
    _matrix: MatrixLike
    _shape: tuple[int,int]

    @property
    def shape(self) -> tuple[int,int]: ...
    @property
    def T(self) -> Matrix: ...

    def __init__(
        self: Matrix,
        matrix: MatrixLike
    ) -> None: ...

    def __eq__(self, __value: object) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __add__(
        self:Matrix,
        other_matrix:Matrix
    ) -> Matrix: ...
    def __mul__(
        self:Matrix,
        other_matrix:Matrix
    ) -> Matrix: ...

    def dot(
        self: Matrix,
        other_matrix: Matrix
    ) -> Matrix: ...
    def add(
        self: Matrix,
        other_matrix: Matrix
    ) -> Matrix: ...