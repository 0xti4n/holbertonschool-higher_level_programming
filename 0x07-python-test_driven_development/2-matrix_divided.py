#!/usr/bin/python3

def matrix_divided(matrix, div):
    new = []
    
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    for li in matrix:
        if type(li) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(li) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) is not int and type(matrix[j][j]) is not float:
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
                else:
                    x = round(matrix[i][j] / div, 2)
                    new.append(list(x))
    return new
