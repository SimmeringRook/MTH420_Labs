# python_intro.py
"""Python Essentials: Introduction to Python.
Thomas Knudson
MTH 420, S2022
22 April 2022
"""
from turtle import left
import numpy as np

#Problem 1

def isolate(a, b, c, d, e)->None:
    """Prints the first three positional arguments with a five space separation and then the last two positional arguments with a single space separator and returns a new line.
    """
    print(a, b, c, sep='     ', end=' ')
    print(d, e, end='\n')


#Problem 2
def first_half(string: str,/)->str:
    """Returns the first half of the given string, excluding the middle character if the length is odd.
    """
    return f'{string[0:int(len(string)/2)]}'


def backward(string: str,/)->str:
    """Returns the given string, but backwards.
    """
    return f'{string[::-1]}'

#Problem 3
def list_ops()->list:
    """Carries out a series of list operations.
    """
    given_list = ["bear", "ant", "cat", "dog"]
    given_list.append("eagle")
    given_list[2] = "fox"
    given_list.pop(1)
    given_list.sort(reverse=True)
    given_list[given_list.index("eagle")] = "hawk"
    given_list.append("hunter")
    return given_list

#Problem 4
def alt_harmonic(n: int)->float:
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    return round(sum([((-1)**(i+1))/i for i in range(1,n+1)]), 5)


def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    return np.where(A > 0, A, 0)


def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0, A^T I |
                                | A  0,  0, |,
                                | B  0,  C |
    where I is the 3x3, identity matrix and each 0, is a matrix of all zeros
    of the appropriate size.
    """
    A = np.arange(0,6).reshape(2,3)
    B = np.tril(np.multiply(3, np.ones((3,3))))
    I = np.eye(3, dtype=int)
    C = np.multiply(-2, I)
    Z33 = np.zeros((3,3))
    Z22 = np.zeros((2,2))
    Z23 = np.zeros((2,3))
    Z32 = np.zeros((3,2))

    #Construct the block columns:
    Z_A_B = np.vstack((Z33, A, B)) # 0, A B
    AT_Z_Z = np.vstack((A.T, Z22, Z32,)) # A^T 0, 0
    I_Z_C = np.vstack((I, Z23, C)) # I 0, C

    return np.hstack((Z_A_B, AT_Z_Z, I_Z_C))


def prob7(A=None):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5,       ,  0.5,       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,,  0.33333333,,  0.33333333,]])
    """
    if A is None:
        A = np.array([[1,1,0],[0,1,0],[1,1,1]])
    return (A.T / np.sum(A, axis=1)).T


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    # I don't have the file, so we're hardcoding it
    grid = np.asarray([8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8, 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0, 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65, 52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91, 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80, 24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50, 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70, 67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21, 24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95, 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92, 16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57, 86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58, 19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40, 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66, 88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36, 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16, 20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54, 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48,]).reshape((20,20))

    #find the maximum product along each direction
    horizontal_max = np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
    vertical_max = np.max(grid.T[:,:-3] * grid.T[:,1:-2] * grid.T[:,2:-1] * grid.T[:,3:])
    #diagonals work by setting the first multiplier to be a 17x17 matrix and then creating the subsequent 17x17's that start off by 1 index from the previous
    right_diag = np.max(grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1,2:-1] * grid[3:,3:])
    left_diag = np.max(grid[:-3,3:] * grid[1:-2,2:-1] * grid[2:-1,1:-2] * grid.T[3:,:-3])

    return np.max([horizontal_max, vertical_max, right_diag, left_diag])

