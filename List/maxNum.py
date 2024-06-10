"""
WAP to find the largest number in a list
"""

mylist = []

n = int(input("Enter the total count of Numbers : "))
# input the list
for i in range(n):
    value = int(input(f"Enter the {i}th no. : "))
    mylist.append(value)


maxNum = mylist[0]
for i in mylist:
    if maxNum < i:
        maxNum = i

print(f"Maximum no. of the list = {maxNum}")
