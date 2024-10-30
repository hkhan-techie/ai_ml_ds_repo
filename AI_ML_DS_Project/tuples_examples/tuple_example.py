# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print()

# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print()

# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print()

# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))
print()

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print()

# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
print()

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print()

# Using the tuple() constructor to make a tuple:

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
print()

## ACCESS TUPLE ITEMS
# Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print()

# Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print()

# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print()

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
print()

# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
print()

# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
print()

# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
print()

# UPDATE TUPLES
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print()

# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
print()

# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
print()

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
print()

# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # this will raise an error because the tuple no longer exists

# Packing and Unpacking
# Packing a tuple:

fruits = ("apple", "banana", "cherry")
print(fruits)
print()

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print()

# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
print()

# Loop tuples_examples
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
print()

# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
print()
print('Print via for loop')
for i in range(len(thistuple)):
    print(thistuple[i])
print()

# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
print()
print('Print via while loop')
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
print()

# Join Tuples
# Join two tuples_examples:

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
print()

# Multiply/duplicate the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print()

numbers = (1, 2, 3)
mynumbers = numbers * 2
print(mynumbers)
print()

# Tuple Methods
# count and index method usage:

thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple.count("apple"))
print(thistuple.index("banana", 0, len(thistuple)))
