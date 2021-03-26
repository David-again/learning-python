#=======================================
# Question 1
#=======================================
def format_address(address_string):
  # Declare variables
  house_num = 0
  street_nom = ""
  # Separate the address string into parts
  address_parts = address_string.split()
  house_num = int(address_parts[0])
  # Traverse through the address parts
  for word in address_parts:
    # Determine if the address part is the
    # house number or part of the street name
    if word.isnumeric(): 
      house_number = int(word)
    else: 
      street_nom += word + " "

  
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_nom)

print('\n')
print("Exercise 1")
print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#=======================================
# Question 2: Emphasize a word by making it uppercase
#=======================================
def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print('\n')
print("Exercise 2")
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#=======================================
# Question 3: Reverse one list, and then merge it to a second list
#=======================================
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  new_list = []
  
  for student_name in list2:
    new_list.append(student_name)
  
  list1.reverse()
  for student_name in list1:
    new_list.append(student_name)
	
  return new_list
  
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print('\n')
print("Exercise 3")
print(combine_lists(Jamies_list, Drews_list))

#=======================================
# Question 4: Use list comprehension to return a list of squares within a given range (inclusive)
#=======================================
def squares(start, end):
	
	return [number * number for number in range(start, end + 1)] 

print('\n')
print("Exercise 4")
print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#=======================================
# Question 5: Process data from a dictionary
#=======================================
def car_listing(car_prices):
  result = ""
  for make_model, price in car_prices.items():
    result += "{} costs ${:,} dollars".format(make_model, price) + "\n"
  return result

print('\n')
print("Exercise 5")
print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

#=======================================
# Question 6: Merge two dictionary, giving preference to the more up-to-date version (Rory's dictionary)
#=======================================
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  new_list = guests2
  new_list.update(guests1)
  # for friend, num_guests in guests2.items():
  #   new_list
  return new_list

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print('\n')
print("Exercise 6")
print(combine_guests(Rorys_guests, Taylors_guests))

#=======================================
# Question 7: Count the frequency of occurency of letters in a string, ignoring upper/lower case. 
#=======================================
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.upper():
    # Check if the letter needs to be counted or not
    if ord(letter) <= 90:
      if ord(letter) >= 65:
        # Check if key already exists or not
        if letter in result:
          result[letter.lower()] += 1
        else:
          result[letter.lower()] = 1 
    # Add or increment the value in the dictionary
    
  return result

print('\n')
print("Exercise 7")
print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

