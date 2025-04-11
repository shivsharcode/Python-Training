# accept a string or number

s = input("Enter the string : ")

s = s.lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("NOT a Palindrome")

