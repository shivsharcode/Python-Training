"""
Write a program to remove the duplicates in a list
"""

mylist = [2, 5, 0, 1, 2, 4, 5, 3]

unique = []

for i in mylist:
    if i not in unique:
        unique.append(i)

print(mylist)
print(unique)


