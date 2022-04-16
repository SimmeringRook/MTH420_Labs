# python_intro.py
"""Python Essentials: Introduction to Python.
<Name>
<Class>
<Date>
"""

#Problem 1
import enum


def isolate(a, b, c, d, e)->None:
    """Prints the first three positional arguements with a five space separation and then the last two positional arguements with a single space separator and returns a new line.
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
    raise NotImplementedError("Problem 5 Incomplete")

def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    raise NotImplementedError("Problem 6 Incomplete")

def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    raise NotImplementedError("Problem 7 Incomplete")


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    raise NotImplementedError("Problem 8 Incomplete")


