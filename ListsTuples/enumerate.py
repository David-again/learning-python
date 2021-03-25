# The enumerate() function assigns an index to each item in an iterable object that can be used to reference the item later. ... It makes it easier to keep track of the content of an iterable object

def skip_elements(elements):
	# code goes here
	new_list = []
	for index, item in enumerate(elements):
		if index % 2 == 0:
			new_list.append(item)
		# print(index)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']

print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']