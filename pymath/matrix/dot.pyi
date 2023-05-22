from typing import TypeAlias

scalar: TypeAlias = int | float | complex
MatrixLike: TypeAlias = list[list[scalar]]

def dot(A: MatrixLike, B: MatrixLike) -> MatrixLike: ...