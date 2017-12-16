### TODO: Write a function called matrix_addition that 
###     calculate the sum of two matrices
###
### INPUTS:
###    matrix A _ an m x n matrix
###    matrix B _ an m x n matrix
###
### OUPUT:
###   matrixSum _ sum of matrix A + matrix B

def matrix_addition(matrixA, matrixB):
    # initialize matrix to hold the results
    matrixSum = []
    
    # matrix to hold a row for appending sums of each element
    row = []
    
    # TODO: write a for loop within a for loop to iterate over
    # the matrices
    for i in range(len(matrixA)):
        for j in range(len(matrixA[0])):
            row.append(matrixA[i][j] + matrixB[i][j])
        matrixSum.append(row)
        row = []
    
    # TODO: As you iterate through the matrices, add matching
    # elements and append the sum to the row variable
    
    # TODO: When a row is filled, append the row to matrixSum. 
    # Then reinitialize row as an empty list
    
    return matrixSum

### When you run this code cell, your matrix addition function
### will run on the A and B matrix.

A = [
    [2,5,1], 
    [6,9,7.4], 
    [2,1,1], 
    [8,5,3], 
    [2,1,6], 
    [5,3,1]
]

B = [
    [7, 19, 5.1], 
    [6.5,9.2,7.4], 
    [2.8,1.5,12], 
    [8,5,3], 
    [2,1,6], 
    [2,33,1]
]

matrix_addition(A, B)