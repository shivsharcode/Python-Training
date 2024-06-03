i = 1
n = int(input("Enter the no. of rows : "))
j = 1
while i <= n:
    print(" " * (n-i), end="")
    print("*" * (2*i-1))
    i += 1

print("done")

