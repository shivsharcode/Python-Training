"""
LIST METHODS
"""

numbers = [1, 4, 5, 9, 0]
# 1. add at the end
numbers.append(99)
print(numbers)

# 2. insert anywhere with index
numbers.insert(0, 10)
print(numbers)

# 3. remove an item
numbers.remove(5)
print(numbers)

# 4. remove last item
numbers.pop()
print(numbers)

# 5. remove all items
numbers.clear()
print(numbers)

numbers = [11, 9, 33, 44, 24]

# 6. check index of an object
print(numbers.index(44))  # will through ValueError is parameter not in the list

# 7. check presence of an object
print(50 in numbers)

# 8. check the total number of objects
print(len(numbers))

# 9. check the count of obj in list
print(numbers.count(22))

# 10. Sort - ascending
numbers.sort()
print(numbers)

# 11. Reverse List
numbers.reverse()
print(numbers)

# 12. copy the list
numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)
