# Creating a list
list = [1, 2, 3, 4, 5]
print("Original list:", list)

# Adding an element to the list
list.append(6)
print("List after adding an element:", list)

# Removing an element from the list
list.remove(3)
print("List after removing an element:", list)

# Modifying an element in the list
list[2] = 10
print("List after modifying an element:", list)

print("\n")

# Creating a dictionary
dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", dict)

# Adding a key-value pair to the dictionary
dict['d'] = 4
print("Dictionary after adding a key-value pair:", dict)

# Removing a key-value pair from the dictionary
del dict['b']
print("Dictionary after removing a key-value pair:", dict)

# Modifying a value in the dictionary
dict['a'] = 10
print("Dictionary after modifying a value:", dict)

print("\n")

# Creating a set
set = {1, 2, 3, 4, 5}
print("Original set:", set)

# Adding an element to the set
set.add(6)
print("Set after adding an element:", set)

# Removing an element from the set
set.remove(3)
print("Set after removing an element:", set)

# Modifying a set (in sets, you cannot directly modify an element, but you can remove and add a new element)
set.remove(2)
set.add(10)
print("Set after modifying an element (remove and add):", set)
