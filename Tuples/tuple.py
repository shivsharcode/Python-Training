"""
TUPLES

Tuple is ordered and immutable collection of values
"""

numbers = (1, 2, 2, 3, 9)

# 1. can get the value at the index but cannot modify them
print(numbers[0])

# 2. if tries modification TypeError will b thrown
try:
    numbers[0] = 11
    print(numbers[0])
except:
    print("TypeError : object does not support item assignment, will be thrown")

# 3. counts the no. of occurrences of a value
print(numbers.count(2))

# 4. index of a value can also be finded
print(numbers.index(9))