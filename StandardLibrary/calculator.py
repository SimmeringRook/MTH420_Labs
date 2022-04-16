"""Python Essentials: The Standard Library.
Thomas Knudson
MTH 420 S2022
April 15, 2022
"""

from math import sqrt

def sum(a: float, b: float,/)->float:
    """Computes the sum of the two floats given.

    Returns:
        float: the arthimetic sum of a and b
    """
    return a+b

def product(a: float, b:float ,/)->float:
    """Computes the scalar product of the two floats given.

    Returns:
        float: the scalar product of a and b
    """
    return a*b

# if __name__ == "__main__":
#     print(sum(1,2))
#     print(product(1,2))