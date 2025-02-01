# ========================================================
# Section 1: Create an array using array() method
# ========================================================

import array as Arr

numbers = Arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # 'i' is the typecode for signed integer
print(numbers)

# ========================================================
# Section 2 : Access elements of the array
# ========================================================

print(numbers[0])
print(numbers[1])

# ========================================================
# Section 3 : Update elements of the array
# ========================================================

numbers[0] = 0
numbers[2] = 100
numbers[3:5] = Arr.array('i', [200, 300])
print(numbers) # output will be array('i', [0, 2, 100, 200, 300, 6, 7, 8, 9, 10])

# ========================================================
# Section 4 : Delete elements of the array
# ========================================================

numbersTwo = Arr.array('i', [50, 60, 70, 80, 90, 100])

del numbersTwo[0]
print(numbersTwo)

# ========================================================
# Section 5 : Find the length of the array
# ========================================================

print(len(numbersTwo)) # Output will be 5

# ========================================================
# Section 6 : Concatenate two arrays
# ========================================================

concatOne = Arr.array('u', ("A", "B", "C")) # 'u' is the typecode for unicode character
concatTwo = Arr.array('u', ("D", "E", "F"))
concatenatedArr = concatOne + concatTwo
print(concatenatedArr)
