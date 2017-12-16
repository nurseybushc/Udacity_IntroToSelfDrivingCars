### TODO: Write a function called inverse_matrix() that 
###       receives a matrix and outputs the inverse
###       
###       You are provided with start code that checks
###       if the matrix is square and if not, throws an error
###
###       You will also need to check the size of the matrix.
###       The formula for a 1x1 matrix and 2x2 matrix are different,
###       so your solution will need to take this into account.
###
###       If the user inputs a non-invertible 2x2 matrix or a matrix
###       of size 3 x 3 or greater, the function should raise an
###       error. A non-invertible
###       2x2 matrix has ad-bc = 0 as discussed in the lesson
###
###       Python has various options for raising errors
###       raise RuntimeError('this is the error message')
###       raise NotImplementedError('this functionality is not implemented')
###       raise ValueError('The denominator of a fraction cannot be zero')

def inverse_matrix(matrix):
    
    inverse = []
    row_len = len(matrix)
    col_len = len(matrix[0])
    if row_len != col_len:
        raise ValueError('The matrix must be square')
    
    ## TODO: Check if matrix is larger than 2x2.
    ## If matrix is too large, then raise an error
    if row_len > 2:
        raise ValueError('The matrix is too large')
    ## TODO: Check if matrix is 1x1 or 2x2.
    ## Depending on the matrix size, the formula for calculating
    ## the inverse is different
    if row_len == 1:
        inverse.append([1.0/matrix[0][0]])
    ## TODO: Calculate the inverse of the square 1x1 or 2x2 matrix.
    else:
        if (matrix[0][0]*matrix[1][1]) == (matrix[0][1] * matrix[1][0]):
            return matrix
        #https://www.mathsisfun.com/algebra/matrix-inverse.html
        # (1/(ad-bc)) * ([[1.1, -0.1],[-1.0, 0.0]])
        determinant = 1.0 / ((matrix[0][0]*matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
        inv_matrix = [[matrix[1][1], -matrix[0][1]],[-matrix[1][0], matrix[0][0]]]
        for i in range(len(inv_matrix)):
            row = []
            for j in range(len(inv_matrix[0])):
                row.append(determinant * inv_matrix[i][j])
            inverse.append(row)
    return inverse
    
    