def identity_matrix(n):
    
    identity = []
    for i in range(n):
        row = []
        for j in range(n):
            if(i != j):
                row.append(0)
            else:
                row.append(1)
        identity.append(row)
    return identity


# TODO: Copy your matrix multiplication function and any other helper
# funcitons here from the previous exercises

def transpose(matrix):
    matrix_transpose = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for j in range(len(matrix)):
            transposed_row.append(matrix[j][i])
        matrix_transpose.append(transposed_row)
        
    
    return matrix_transpose

def get_row(matrix, row):
    return matrix[row]

def dot_product(vector_one, vector_two):
    sum = 0
    for i in range(len(vector_one)):
        sum += vector_one[i]* vector_two[i]
    return sum



def matrix_multiplication(matrixA, matrixB):
    product = []
    
    matrixBT = transpose(matrixB)
    
    m_rows = len(matrixA)
    p_columns = len(matrixBT)
    
    
    for i in range(len(matrixA)):
        row_result = []
        for j in range(len(matrixBT)):
            row = get_row(matrixA, i)
            row2 = get_row(matrixBT, j)
            dt = dot_product(row, row2)
            row_result.append(dt)
        product.append(row_result)
    return product