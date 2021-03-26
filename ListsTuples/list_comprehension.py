multiples = []
for x in range(1,11):
    multiples.append( x * 7 )
print(multiples)

# The below line achieves the same as above snippet!
series = [ y * 7 for y in range(1,11) ]
print(series)   # returns as a list of integers, a series of the first ten multiples of 7 