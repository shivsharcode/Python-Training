text = input("Enter text : ")

base = 200
prime = 101

textHash = 0

for i in range(len(text)):
    textHash = ((textHash * base) + ord(text[i])) % prime
    print(textHash)

print("final textHash = ", textHash)
