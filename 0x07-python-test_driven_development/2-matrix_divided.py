#!/usr/bin/python3
"""function that divides all elements of a matrix
if the parameters pass all the filters the program return
the division of 2 integers or floats
if the number is zero return an erorr
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    and return the division if not error ocurred
    """
    m1 = "div must be a number"
    m2 = "division by zero"
    m3 = "matrix must be a matrix (list of lists) of integers/floats"
    m4 = "Each row of the matrix must have the same size"
    m5 = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is not None:
        if type(div) is not int and type(div) is not float:
            raise TypeError(m1)
        if div == 0:
            raise ZeroDivisionError(m2)
        if type(matrix) is not list or len(matrix) == 0:
            raise TypeError(m3)

        for li in matrix:
            if type(li) is not list or len(li) == 0:
                raise TypeError(m3)
            elif len(li) != len(matrix[0]):
                raise TypeError(m4)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ma = matrix[i][j]
                if type(ma) is not int and type(ma) is not float:
                    raise TypeError(m5)

        return list(map(lambda i: list(map
                        (lambda j: round(j / div, 2), i)), matrix))
    else:
        raise TypeError(m3)
