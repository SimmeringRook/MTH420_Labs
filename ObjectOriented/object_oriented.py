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
        self.contents = list()
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
        self.contents = list()

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
    print(f"Contents: {testpack.contents}")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item) # Test capacity.
    testpack.dump()
    print(f"Contents: {testpack.contents}")

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
class Jetpack(Backpack):
    """A Jetpack that inherits from Backpack. In addition to storing information about the owner and contents stored inside, the jetpack can also hold an amount of fuel that can be used for flying.
    
    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
        color (str): the color of the backpack
        max_size (int): the integer capacity of items the backpack can hold. Defaults to 5.
        amount_of_fuel (float): the amount of fuel that can be used to fly. Defaults to 10.
    """
    
    def __init__(self, name: str, color: str, amount_of_fuel: float=10, max_size: int = 5):
        """Creates a jetpack that has the same properties of a backpack but can also hold fuel and fly.

        Args:
            name (str): The owner's name.
            color (str): The color of the jetpack.
            amount_of_fuel (float, optional): The amount of fuel stored in the jetpack. Defaults to 10.
            max_size (int, optional): The maximum capacity for storage of items. Defaults to 5.
        """
        super().__init__(name, color, max_size)
        self.amount_of_fuel = amount_of_fuel
    
    def put(self, item)->None:
        """Places the item in storage, if the pack is not at full capacity. If the pack is full, the item will not be added and a message will print

        Args:
            item (_type_): the item to add to the pack
        """
        super().put(item)
    
    def fly(self, fuel_to_burn: float)->None:
        """Will fly for the amount of fuel given, if the amount is not greater than what the jetpack currently has. If the request amount of fuel to fly is greater than what is available, the jetpack will not fly at all.

        Args:
            fuel_to_burn (float): amount of fuel to use for flight
        """
        if fuel_to_burn > self.amount_of_fuel:
            print("Not enough fuel!")
            return
        self.amount_of_fuel -= fuel_to_burn
        
    def dump(self)->None:
        """Dumps both the stored contents and any remaining fuel.
        """
        self.amount_of_fuel = 0
        super().dump()

def test_jetpack():
    test_jetpack = Jetpack("Barry", "black") # Instantiate the object.
    if test_jetpack.name != "Barry": # Test an attribute.
        print("Backpack.name assigned incorrectly")
    print(f"{test_jetpack.contents}, {test_jetpack.max_size=}")
    for item in ["pencil", "pen", "paper", "computer"]:
        test_jetpack.put(item) # Test a method.
    print(f"Contents: {test_jetpack.contents}")
    for item in ["pencil", "pen", "paper", "computer"]:
        test_jetpack.put(item) # Test capacity.
    print(f'Fuel remaining: {test_jetpack.amount_of_fuel}')
    test_jetpack.fly(3)
    print(f'Fuel remaining: {test_jetpack.amount_of_fuel}')
    test_jetpack.fly(10)
    print(f'Fuel remaining: {test_jetpack.amount_of_fuel}')
    test_jetpack.dump()
    print(f"Contents: {test_jetpack.contents}")
    print(f'Fuel remaining: {test_jetpack.amount_of_fuel}')

# Problem 4: Write a 'ComplexNumber' class.
class ComplexNumber:
    
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imag = imaginary
    
    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)
    
    def __str__(self):
        if self.imag < 0:
            return f'({self.real}{self.imag}j)'
        return f'({self.real}+{self.imag}j)'
    
    def __abs__(self):
        from math import sqrt
        return sqrt((self.real**2) + (self.imag**2))
    
    def __eq__(self, other):
        if not isinstance(other, self):
            raise TypeError("ComplexNumbers can only be compared against other ComplexNumbers (or those that inherit from it)")
        return (self.real == other.real) and (self.imag == other.imag)
    
    def __add__(self, other):
        if not isinstance(other, self):
            raise TypeError("ComplexNumbers can only be added with other ComplexNumbers (or those that inherit from it)")
        return ComplexNumber(self.real+other.real, self.imag+other.imag)
     
    def __sub__(self, other):
        if not isinstance(other, self):
            raise TypeError("ComplexNumbers can only be subtracted from other ComplexNumbers (or those that inherit from it)")
        return ComplexNumber(self.real-other.real, self.imag-other.imag)
     
    def __mul__(self, other):
        if not isinstance(other, self):
            raise TypeError("ComplexNumbers can only be multiplied with other     ComplexNumbers (or those that inherit from it)")
        return ComplexNumber(self.real*other.real, self.imag*other.imag)
    
    def __truediv__(self, other):
        if not isinstance(other, self):
            raise TypeError("ComplexNumbers can only be divided from other     ComplexNumbers (or those that inherit from it)")
        return ComplexNumber(self.real/other.real, self.imag/other.imag)
