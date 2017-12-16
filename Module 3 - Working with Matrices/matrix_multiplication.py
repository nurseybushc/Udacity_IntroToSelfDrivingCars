
def get_row(matrix, row):
    return matrix[row]

def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

def dot_product(vector_one, vector_two):
    sum = 0
    for i in range(len(vector_one)):
        sum += vector_one[i]* vector_two[i]
    return sum

def matrix_multiplication(matrixA, matrixB):
    
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])
    
    result = []
    
    for i in range(m_rows):
        row_result = []
        for j in range(p_columns):
            row = get_row(matrixA,i)
            col = get_column(matrixB, j)
            dt = dot_product(row, col)
            row_result.append(dt)
        result.append(row_result)
        row_result = []
    
    return result