# Creating an empty list
arr = []

# Creating an array with initial elements
arr = [1, 2, 3, 4, 5]


# Accessing elements by index (0-based)
first_element = arr[0]  # 1
last_element = arr[-1]  # 5

# Modifying an element at a specific index
arr[1] = 10  # arr becomes [1, 10, 3, 4, 5]

# Adding an element to the end of the list
arr.append(6)  # arr becomes [1, 10, 3, 4, 5, 6]

# Inserting an element at a specific position
arr.insert(2, 15)  # arr becomes [1, 10, 15, 3, 4, 5, 6]

# Removing an element by value
arr.remove(10)  # arr becomes [1, 15, 3, 4, 5, 6]

# Removing an element by index
removed_element = arr.pop(2)  # arr becomes [1, 15, 4, 5, 6], removed_element is 3

# Finding the index of a value
index_of_4 = arr.index(4)  # 2

# Counting occurrences of a value
count_of_6 = arr.count(6)  # 1

# Slicing to get a sublist
subArray = arr[1:4]  # [15, 4, 5]

# Iterating through the list
for element in arr:
    print(element)

# Iterating with index
for i, element in enumerate(arr):
    print(f"Index {i}: {element}")


# Reversing the order of elements
arr.reverse()  # arr becomes [1, 4, 5, 6, 15]

# Concatenating two lists
arr2 = [7, 8, 9]
concatenated = arr + arr2  # concatenated becomes [1, 4, 5, 6, 15, 7, 8, 9]

# Checking if an element is in the list
exists = 5 in arr  # True

# Creating a shallow copy of the list
arr_copy = arr.copy()  # arr_copy becomes [1, 4, 5, 6, 15]


# Sorting in ascending order
arr.sort()  # arr becomes [1, 4, 5, 6, 15]

# Sorting in descending order
arr.sort(reverse=True)  # arr becomes [15, 6, 5, 4, 1]
