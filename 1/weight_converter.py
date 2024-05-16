# Ask a user their weight (in kilograms), convert it to pounds and print on the terminal

weightType = input("Enter 'p' for Pounds and 'k' for Kilograms : ").lower()
wt = float(input(f"Enter your weight : "))

if (weightType == 'k') :
    wt_pounds = wt * 2.2046
    print(f"Your Weight in Pounds = {wt_pounds}")
elif (weightType == 'p') :
    wt_kilograms = wt / 2.2046
    print(f"Your Weight in Kilograms = {wt_kilograms}")
else :
    print("Wrong Input :( ")

