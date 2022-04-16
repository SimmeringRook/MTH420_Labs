# object_oriented.py
"""Python Essentials: Object Oriented Programming.
Thomas Knudson
MTH 420, S2022
April 15, 2022
"""


class Backpack:
    """A Backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
        color (str): the color of the backpack
        max_size (int): the integer capacity of items the backpack can hold
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name: str, color: str, max_size: int=5,):
        """Set the name and initialize an empty list of contents.

        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int): the maximum item capacity for the backpack.
        """
        self.name = name
        self.contents = []
        self.color = color
        self.max_size= max_size

    def put(self, item)->None:
        """Add an item to the backpack's list of contents, if there is room."""
        if len(self.contents) == self.max_size:
            print("No Room!")
            return
        self.contents.append(item)

    def take(self, item)->None:
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)
        
    def dump(self)->None:
        """Removes all items from the backpack's list of contents."""
        self.contents = [ ]

    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)

def test_backpack():
    testpack = Backpack("Barry", "black") # Instantiate the object.
    if testpack.name != "Barry": # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item) # Test a method.
    print("Contents:", testpack.contents)
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item) # Test capacity.
    testpack.dump()
    print("Contents:", testpack.contents)

# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum(len(str(item)) for item in self.contents)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.


# Problem 4: Write a 'ComplexNumber' class.
