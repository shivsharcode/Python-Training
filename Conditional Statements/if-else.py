'''
if the day is hot - message to drink enough water
otherwise if it's cold - msg to wear warm clothes
otherwise it would be a lovely day

'''

day = input("Enter 'h' if it's a 🔥 hot day OR \nEnter 'c' if it's a ❄️cold day \nOR enter any key it's neither🌸 \nEnter : ").lower()

if day == 'h':
    print("It's a hot day 🥵")
    print("Drink plenty of water💧")
elif day == 'c':
    print("It's a cold day 🥶")
    print("Wear warm clothes 🧣")
else:
    print("It's a lovely day 😌")

