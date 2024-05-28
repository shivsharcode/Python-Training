"""
If temperature is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold
"""

temp = float(input("Enter the Temp 🌡️ in Cel : "))

if temp > 30:
    print("It's a hot day 🥵 ")
elif temp < 10:
    print("It's a cold day 🥶")
else:
    print("It's a pleasant day 😌")
