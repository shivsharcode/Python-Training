
s = input("Enter string : ")


mid = len(s)
n = len(s)
i = 0
isPalindrome = True
while i < mid:
    if s[i] == s[n-1-i]:
        pass
    else:
        isPalindrome = False

    i += 1


if isPalindrome:
    print("Palindrome")
else:
    print("Not a palindrome")