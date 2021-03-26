def squares(start, end):
	# for number in range(start, end + 1):
	# scratch that!  No need for any for loops!

    # squares = [number * number for number in range(start, end + 1)]
	return [number * number for number in range(start, end + 1)] 

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]