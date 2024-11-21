from collections import Counter

mydict = {'banana': 3,
          'apple': 5,
          'cherry': 2
          }

print(mydict)
print(mydict.items())
print(mydict.keys())
print(mydict.values())

sorted_by_key_length = dict(sorted(mydict.items(), key=lambda item: len(item[0]) ))
print(sorted_by_key_length)

