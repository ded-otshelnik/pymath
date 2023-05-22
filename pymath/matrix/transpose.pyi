from typing import TypeAlias

MatrixLike: TypeAlias = list[list]

def transpose(A:MatrixLike) -> MatrixLike: ...