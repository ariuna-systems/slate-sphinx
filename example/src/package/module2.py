"""
This is a :mod:`package.module2` documentation example.
"""

from typing import List, Tuple, Union, TypeVar


CustomTypeAlias = Union[List[str], Tuple[int, int]]
"""This is a type alias."""


CustomTypeVariable = TypeVar("CustomTypeVariable", bound=int)
"""This is a type variable."""


CONSTANT: str = "constant"


def function(argument1: int = 1, argument2: float = 1.0) -> None:
    """
    The function documentation example.

    $y = \sin(x)$

    :param argument1: The argument1
    :param argument2: The argument2

    :raise: SomeException

    :return: None
    """


class Error(Exception):
    """Custom exception."""


class Example:
    """
    The class documentation example.
    """

    def example(self) -> None:
        """
        The method documentation example.
        """
