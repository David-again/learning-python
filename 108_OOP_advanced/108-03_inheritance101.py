# Inheritance is implemented in the class declaration by putting the ancestor class in parenthesis.  Example below, Apple inherits from the Fruit class.

class Fruit: 
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

granny_smith = Apple("green", "tart")
print(granny_smith.flavor) # should print 'tart'

# Note: In python, the pass is a null statement, used within a function that will be implemented in the future.