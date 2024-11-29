from collections.abc import Iterable
from typing import TypeVar

_T = TypeVar("_T")


def as_list(
    x: _T | Iterable[_T], base_type: tuple[type, ...] = (str, bytes)
) -> list[_T]:
    if isinstance(x, base_type):
        return [x]  # pyright: ignore [reportReturnType]
    if isinstance(x, Iterable):
        return list(x)
    return [x]
