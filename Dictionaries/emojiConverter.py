"""
EMOJI CONVERTOR
"""

message = input(">")
words = message.split(' ')  # split splits the string into words and returns a list

emojis = {
    ":)": "☺️",
    ":(": "😔",
    ":|": "😑"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)


