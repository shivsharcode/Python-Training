i = 1
n = int(input("Enter the no. of rows : "))
while i <= n:
    print(' ' * (n-i), end="")
    print("*" * i)
    i += 1

print('done')
