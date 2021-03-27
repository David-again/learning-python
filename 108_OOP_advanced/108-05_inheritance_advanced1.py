# The Piglet and Cow classes below inherit from the Animal class. They each have a unique 'sound' property too.

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak() # should return "Oink! I'm Hamlet! Oink!"

class Cow(Animal):
    sound = "Moooo!"

milky = Cow("Milky White")
milky.speak() #should return "Moooo! I'm Milky White! Moooo"