sentence = 'Python for Beginners'

print(sentence)
print(sentence.upper())  # to upper case
print(sentence.lower())  # to lower case
print(sentence.find('B'))  # find the position of 'B' in the string
print(sentence.find('z'))  # will return -1 as 'z' is not in the string
print(sentence.replace('Beginners', 'Coders'))  # will return a replaced string as the arguments sugggest
print(sentence)

print('Python' in sentence)  # returns a boolean value to check whether it is in it or not
print(len(sentence))
