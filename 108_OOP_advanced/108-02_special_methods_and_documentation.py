# ======================
# The __str__() method
# ======================
# The __str__ method is called when the following functions are invoked on the object and return a string:
    # print()
    # str()

# See example below:

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold) # should return: "This apple is red and its flavor is sweet"

# Had the __str__ method not been defined, print() would have returned a reference to the memory location where the instance of the class is stored, which is not necessarily useful information!  See the example below:

class Orange:
    def __init__(self, color):
        self.color = color

osan = Orange("yellow")
print(osan)
# result:
# <__main__.Orange object at 0x000001E54154DC40>
# ...not so useful, no?


# ==========
# DOCSTRINGS
# ==========
# Docstrings serve as documentation for our function/class/method.  It is basically a string enclosed in triple quotes in the definition of the function.  See example below:

def to_seconds(hours, mins, secs):
    """Returns the amount of seconds in the given hours, minutes and seconds"""
    return hours * 3600 + mins * 60 + secs 

# Now, this docstring will be displayed when the following is typed at the Python CLI:

# help(to_seconds)
# Note the indentation of the docstring: must be same as the method it is documenting.