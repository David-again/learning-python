file_counts = { "jpg": 10, "txt": 14, "csv": 2, "py": 23 }
for extension in file_counts:
    print(extension)
    
# Note: The above only returns the keys of the dictionary by default.
# In the alternative, we can use the .items() method to get a tuple of key: value pairs, which is "unpacked" at the initialization of the for loop.  See example:

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

# further reading necessary for the two lines of code below:
#Question: what data types are they?

print(file_counts.keys())
# dict_keys(['jpg', 'txt', 'csv', 'py'])

print(file_counts.values())
# dict_values([10, 14, 2, 23])

# Check if a certain key already exists in the dictionary.
print(file_counts["jpg"])
variable = "py"
print(file_counts[variable])
if "xls" in file_counts:
    print("Key found")
    print(file_counts["xls"])
else: 
    print("Key not found")