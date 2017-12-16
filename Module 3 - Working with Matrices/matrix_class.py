import math
from math import sqrt
from copy import deepcopy
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

#for mul start
def get_row(matrix, row):

    return matrix[row]

def get_col(matrix, column_number):
    column = []
    for i in range(matrix.h):
        column.append(matrix[i][column_number])
    return column

def dot_product(vector_one, vector_two):
    sum = 0
    min = len(vector_one)
    if(len(vector_one) > len(vector_two)):
        min = len(vector_two)
    for i in range(min):
        sum += vector_one[i] * vector_two[i]
    return sum
#for mul end
    
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        #print("determinant")
        #print(self)
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if (self[0][0]*self[1][1]) == (self[0][1] * self[1][0]):
            raise(ValueError, "ad=bc.")
        
        determinant = 1.0 / ((self[0][0]*self[1][1]) - (self[0][1] * self[1][0]))
        return determinant
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        sum = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    sum += self.g[i][j]
        return sum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        inverse = deepcopy(self)
        if self.h == 1:
            inverse[0][0] = 1.0/self[0][0]
        else:
            if (self[0][0]*self[1][1]) == (self[0][1] * self[1][0]):
                return self

            inv_matrix = [[self[1][1], -self[0][1]],[-self[1][0], self[0][0]]]
            for i in range(len(inv_matrix)):
                for j in range(len(inv_matrix[0])):
                    inverse[i][j] = self.determinant() * inv_matrix[i][j]
        
        return inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_T = deepcopy(self)
        for i in range(self.w):
            for j in range(self.h):
                matrix_T[i][j] = self[j][i]
    
        return matrix_T

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        """
        print("matrixA")
        print(self)
        print("matrixB")
        print(other)
        """
        
        new_matrix = deepcopy(self)

        for i in range(new_matrix.h):
            for j in range(new_matrix.w):
                new_matrix.g[i][j] += other.g[i][j]
        return new_matrix

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        new_matrix = deepcopy(self)
        for i in range(new_matrix.h):
            for j in range(new_matrix.w):
                new_matrix[i][j] *= -1
        return new_matrix

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + (-other)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        
        rows = other.h
        columns = self.w

        new_matrix = zeroes(self.h,other.w)
        
        for i in range(new_matrix.h):
            for j in range(new_matrix.w):
                vector_row = get_row(self, i)
                vector_col = get_col(other, j)
                new_matrix[i][j] = dot_product(vector_row, vector_col)
        
        return new_matrix

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            matrix = deepcopy(self)
            for i in range(self.h):
                for j in range(self.w):
                    matrix[i][j] = other * self[i][j]
            return matrix
            