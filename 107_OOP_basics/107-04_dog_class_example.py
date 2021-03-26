# This is a Dog class, with a dog_years() method to convert the dog's age to dog-years. (one human year is about 7 dog years).

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())