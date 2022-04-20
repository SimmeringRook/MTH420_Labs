# python_intro.py
"""Python Essentials: Introduction to Python.
Thomas Knudson
MTH 420, S2022
April 1, 2022
"""

"""
## Problem 1:
Volume of a sphere
"""

def get_volume_of_sphere(radius: float) -> float:
    pi,scale_factor = 3.14159, 4/3
    return scale_factor * pi * (radius ** 3)

if __name__ == '__main__':
    V = get_volume_of_sphere(radius=10)
    print(f'{V=}')
    
"""
## Problem 2:
Print hello world
"""

if __name__ == '__main__':
    print("Hello World!")

"""
## Problem 3:
Rewrite Problem 1 as a function
"""

def sphere_volume(radius: float)->float:
    return get_volume_of_sphere(radius)

if __name__ == '__main__':
    print(sphere_volume(10))
    
"""
## Problem 4:

Define two matrices,

\begin{equation}
A = \begin{pmatrix} 3 & -1 & 4 \\ 1 & 5 & -9 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 6 & -5 & 3 \\ 5 & -8 & 9 & 7 \\ 9 & -3 & -2 & -3 \end{pmatrix},
\end{equation}

and use NumPy to carry out the matrix multiplication.
"""

import numpy as np

def prob4(A=None, B=None):
    if A is None:
        A = np.array([[3, -1, 4], [1,5,-9]])
    if B is None:
        B = np.array([[2,6,-5,3], [5,-8,9,7], [9,-3,-2,-3]])
    return get_product_of_A_and_B(A=A, B=B)

def get_product_of_A_and_B(*, A=None, B=None):
    return np.dot(A, B)

if __name__ == "__main__":
    A = np.array([[3, -1, 4], [1,5,-9]])
    B = np.array([[2,6,-5,3], [5,-8,9,7], [9,-3,-2,-3]])
    print(prob4())
    
"""
## Problem 5:

The United States tax system is a progressive tax, meaning the more money an individual makes, the higher percentage that money is taxed at. For 2021, the first three tax brackets for a single person filing their taxes are:

| Tax Rate | Taxable Income |
| --- | --- |
| 10% | Up to $9,875 |
| 12% | $9,875.01 to $40.125 |
| 22% | $40,125.01 to $85,525 |

For example, assume you are single and have a taxable income of $63,000. The first $9,875 you earn is taxed at the 10% rate, so that’s $987.5. The next $30,249.99 (the difference between $40,125 and $9,875.01) is taxed at the 12% rate, which will add an additional $3,630. The last $22,875 will be taxed at the 22% rate, which will be $5,032.5. Your total tax liability is then $9,650.

Write a function called tax_liability() that accepts a single parameter, income, and returns the tax liability. To keep this problem simple, assume the individual is always single, and only use the three tax brackets discussed here (so everything above $85,525 will still be taxed at the 22% rate).
"""

def tax_liability(income: float) -> float:
    high_bracket_threshold, high_bracket_rate = 40125, round(0.22, 2)
    medium_bracket_threshold, medium_bracket_rate = 9875, round(0.12, 2)
    low_bracket_rate = round(0.10, 2)
    liability = 0

    if income > medium_bracket_threshold:
        liability = medium_bracket_threshold * low_bracket_rate
    else:
        return income * low_bracket_rate

    if (income - medium_bracket_threshold) > (high_bracket_threshold - medium_bracket_threshold):
        liability += (high_bracket_threshold - medium_bracket_threshold) * medium_bracket_rate
    else:
        return liability + (income - medium_bracket_threshold) * medium_bracket_rate
    
    if income > high_bracket_threshold :
        liability += (income - high_bracket_threshold) * high_bracket_rate
    
    return liability

"""
## Problem 6:

Now that we have seen how to use lists and NumPy arrays, let’s compare their abilities. Below are vectors A and B, write a function called `prob6a()` that defines them using the Python list data type. Use list comprehension to define the vectors. Return $A \cdot B$, $A + B$, and $5A$.

In a separate function called `prob6b()` define A and B as NumPy arrays and return the $A \cdot B$, $A + B$, and $5A$.

\begin{equation}
A = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 \end{pmatrix}, \qquad B = \begin{pmatrix} 5 & 5 & 5 & 5 & 5 & 5 & 5 \end{pmatrix}
\end{equation}

Check the values of both functions are the same. Notice that one method is much more simple than the other.
"""

def prob6a():
    A = [x for x in range(1,8)]
    B = [5 for x in range(1,8)]
    
    dot_product = 0
    for a_i,b_i in zip(A,B):
        dot_product += a_i * b_i
        
    matrix_sum = [a_i+b_i for a_i, b_i in zip(A,B)]

    scaled_A = [5*x for x in range(1,8)]

    return (dot_product, matrix_sum, scaled_A)

def prob6b():
    A = np.arange(1,8)
    B = 5*np.ones((7))
    
    dot_product = np.dot(A,B)
    matrix_sum = np.add(A, B)
    scaled_A = 5*A

    return (dot_product, matrix_sum, scaled_A)    

if __name__ == "__main__":
    print(prob6a())
    print(prob6b())
