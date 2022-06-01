#include <iostream>
#include <random>

// Function that generates square matrix of integers given its size
// Input: size of the matrix
// Output: square matrix of integers

// Function that prints a matrix given its size and the matrix itself
void print_matrix(int **matrix, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void print_matrix(const int **matrix, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}


extern "C"
{
    int **generate_matrix(int size)
    {
        int **matrix = new int *[size];
        for (int i = 0; i < size; i++)
        {
            matrix[i] = new int[size];
        }
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                matrix[i][j] = rand() % 10;
            }
        }
        return matrix;
    }

    // Function that performs matrix multiplication given two matrices.
    // The function should be able to accept square matrices of any size.
    int **matrix_multiply(const int **matrix_a, const int **matrix_b, int **matrix_c, const int size)
    {
        print_matrix(matrix_a, size);
        print_matrix(matrix_b, size);

        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                for (int k = 0; k < size; k++)
                {
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j];
                }
            }
        }
        print_matrix(matrix_c, size);
        return matrix_c;
    }

    // Given two square matrices and their sizes, the function should return the
    // sum of the matrices as a new matrix.
    int **matrix_add(const int **matrix_a, const int **matrix_b, const int size)
    {
        int **matrix_c = new int *[size];
        for (int i = 0; i < size; i++)
        {
            matrix_c[i] = new int[size];
        }
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j];
            }
        }
        return matrix_c;
    }

    // Apply threshold to matrix, if value is less than threshold, set it to value
    // else set it to abs(1 - value). Return new matrix as a result.
    int **apply_threshold(const int **matrix, const int size, const int threshold, const int value)
    {
        int **matrix_c = new int *[size];
        for (int i = 0; i < size; i++)
        {
            matrix_c[i] = new int[size];
        }
        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
            {
                if (matrix[i][j] < threshold)
                {
                    matrix_c[i][j] = value;
                }
                else
                {
                    matrix_c[i][j] = abs(1 - value);
                }
            }
        }
        return matrix_c;
    }
}
// main function
int main()
{
//     int size = 10;
//     int **matrix_a = generate_matrix(size);
//     int **matrix_b = generate_matrix(size);
//     int **matrix_c = matrix_multiply(matrix_a, matrix_b, size);
//     int **matrix_d = apply_threshold(matrix_c, size, 200, 0);
//     int **matrix_e = apply_threshold(matrix_c, size, 200, 1);
//     int **matrix_f = matrix_add(matrix_d, matrix_e, size);
    return 0;
}
