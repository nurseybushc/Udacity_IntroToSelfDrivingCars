#include "matrix_addition_improved.h"

using namespace std;

vector < vector <int> > matrix_addition_improved (vector < vector <int> > matrixa, vector < vector <int> > matrixb) {
    int rows_a, rows_b, cols_a, cols_b;
    // store the number of rows and columns in the matrices
    rows_a = matrixa.size();
    rows_b = matrixb.size();
    cols_a = matrixa[0].size();
    cols_b = matrixb[0].size();

    // if both matrices have the same size, calculate and return the sum
    // otherwise check if the number of rows and columns are not equal and return a matrix of zero
    if (rows_a == rows_b && cols_a == cols_b) {
        for (unsigned int i = 0; i < rows_a; i++) {
            for (unsigned int j = 0; j < cols_a; j++) {
              matrixa[i][j] += matrixb[i][j];
            }
        }
      return matrixa;
    }
  	return vector <vector <int> >(rows_a,vector<int>(cols_b));
}
