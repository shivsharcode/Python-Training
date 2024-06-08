"""

"""

prices = []

# take the prices
itemCount = int(input("Enter the no. of items : "))

for i in range(itemCount):
    item = float(input(f"Enter the price of item-{i+1} :"))
    prices.append(item)

print(f"Total Price = {sum(prices)} ")
