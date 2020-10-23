"""
If we are presented with the first k terms of a sequence it is impossible to say with
certainty the value of the next term, as there are infinitely many polynomial functions
that can model the sequence.

As an example, let us consider the sequence of cube
numbers. This is defined by the generating function,
u(n) = n3: 1, 8, 27, 64, 125, 216, ...

Suppose we were only given the first two terms of this sequence. Working on the
principle that "simple is best" we should assume a linear relationship and predict the
next term to be 15 (common difference 7). Even if we were presented with the first three
terms, by the same principle of simplicity, a quadratic relationship should be
assumed.

We shall define OP(k, n) to be the nth term of the optimum polynomial
generating function for the first k terms of a sequence. It should be clear that
OP(k, n) will accurately generate the terms of the sequence for n ≤ k, and potentially
the first incorrect term (FIT) will be OP(k, k+1); in which case we shall call it a
bad OP (BOP).

As a basis, if we were only given the first term of sequence, it would be most
sensible to assume constancy; that is, for n ≥ 2, OP(1, n) = u(1).

Hence we obtain the
following OPs for the cubic sequence:

OP(1, n) = 1            1, 1, 1, 1, ...
OP(2, n) = 7n-6         1, 8, 15, ...
OP(3, n) = 6n^2-11n+6   1, 8, 27, 58, ...
OP(4, n) = n^3          1, 8, 27, 64, 125, ...

Clearly no BOPs exist for k ≥ 4.

By considering the sum of FITs generated by the BOPs (indicated in red above), we
obtain 1 + 15 + 58 = 74.

Consider the following tenth degree polynomial generating function:

1 - n + n^2 - n^3 + n^4 - n^5 + n^6 - n^7 + n^8 - n^9 + n^10

Find the sum of FITs for the BOPs.
"""


from typing import Callable, List

import numpy as np


def interpolate(y_list: List[int]) -> Callable[[int], int]:
    """
    Given a list of data points (1,y0),(2,y1), ..., return a function that
    interpolates the data points. We find the coefficients of the interpolating
    polynomial by solving a system of linear equations corresponding to
    x = 1, 2, 3...

    >>> interpolate([1])(3)
    1
    >>> interpolate([1, 8])(3)
    15
    >>> interpolate([1, 8, 27])(4)
    58
    >>> interpolate([1, 8, 27, 64])(6)
    216
    """

    size: int = len(y_list)
    A: np.ndarray = np.zeros(size * size).reshape(size, size)
    b: np.ndarray = np.zeros(size).reshape(size, 1)
    a: np.ndarray
    i: int
    y: int

    for i, y in enumerate(y_list):
        for j in range(size):
            A[i][j] = (i + 1) ** (size - j - 1)
        b[i] = y

    a = np.dot(np.linalg.inv(A), b)

    return lambda x: sum(round(a[i][0]) * (x ** (size - i - 1)) for i in range(size))


def u(n: int) -> int:
    """
    The generating function u as specified in the question.
    >>> u(0)
    1
    >>> u(1)
    1
    >>> u(5)
    8138021
    >>> u(10)
    9090909091
    """
    return (
        1
        - n
        + n ** 2
        - n ** 3
        + n ** 4
        - n ** 5
        + n ** 6
        - n ** 7
        + n ** 8
        - n ** 9
        + n ** 10
    )


def solution(func: Callable[[int], int] = u, order: int = 10) -> int:
    """
    Find the sum of the FITs of the BOPS. For each interpolating polynomial of order
    1, 2, ... , 10, find the first x such that the value of the polynomial at x does
    not equal u(x).
    >>> solution(lambda n: n ** 3, 3)
    74
    """
    data_points: List[int] = list(map(func, range(1, order + 1)))

    polynomials: List[Callable[[int], int]] = [
        interpolate(data_points[:i]) for i in range(1, order + 1)
    ]

    ret: int = 0
    i: int
    x: int

    for i in range(order):
        x = 1
        while func(x) == polynomials[i](x):
            x += 1

        ret += polynomials[i](x)

    return ret


if __name__ == "__main__":
    print(f"{solution() = }")
