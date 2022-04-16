# standard_library.py
"""Python Essentials: The Standard Library.
Thomas Knudson
MTH 420 S2022
April 15, 2022
"""


# Problem 1
from itertools import combinations, permutations


def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    if not isinstance(L, list):
        raise ValueError("L must be a list")
    # Assume L contains values that can be summed
    return min(L), max(L), (sum(L)/len(L))

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    number = 0
    number_2 = number
    number += 1
    integers_are_mutable = (number_2 is number)
    
    some_string = 'abc'
    not_the_same_string = some_string
    some_string = 'ab'
    strings_are_mutable = (some_string is not_the_same_string)
    
    list_a = [ ]
    list_b = list_a
    list_a.append("a")
    lists_are_mutable = (list_a is list_b)
    
    tuple_a = (1,)
    tuple_b = tuple_a
    tuple_a += (1,)
    tuples_are_mutable = (tuple_a is tuple_b)
    
    set_a = set(list_a)
    set_b = set_a
    set_a.add("b")
    sets_are_mutable = (set_a is set_b)
    
    results = f'{integers_are_mutable=} \n {strings_are_mutable=} \n {lists_are_mutable=} \n {tuples_are_mutable=} \n {sets_are_mutable=}'
    print(results)

# Problem 3

def hypot(a, b,/):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    import calculator
    return calculator.sqrt(calculator.sum(calculator.product(a,a), calculator.product(b,b)))

# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    from itertools import combinations
    power_set = [ ]
    for i, _ in enumerate(A):
        for combination in combinations(A, i):
            print(combination)
            power_set.append(combination)
    power_set.append(A)
    return power_set


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""