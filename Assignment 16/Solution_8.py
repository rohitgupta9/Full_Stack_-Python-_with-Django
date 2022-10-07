# Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

# Python program to sort a list of
# tuples by the second Item using sorted()

# Function to sort the list by second item of tuple
def Sort_Tuple(tup):

	# reverse = None (Sorts in Ascending order)
	# key is set to sort using second element of
	# sublist lambda has been used
	return(sorted(tup, key = lambda x: x[1]))

# Driver Code
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

# printing the sorted list of tuples
print(Sort_Tuple(tup))

