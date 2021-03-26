# Here's a person class with an attribute 'name', which is set at the time an object is constructed.  Furthermore, it has a greeting() method that uses the assigned name!

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + self.name

# Create a new instance with a name of your choice
some_person = Person("Dracula")
# Call the greeting method
print(some_person.greeting())
