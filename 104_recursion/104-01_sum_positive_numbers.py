def sum_positive_numbers(n):
  if (n<=1):
    #base case
    return 1
  #recursive case
  # return 0
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
print(sum_positive_numbers(-24)) # Should be 15
