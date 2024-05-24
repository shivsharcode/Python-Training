""" Price of a house is $1M, If buyer has good credit they need to put down 10 %
Otherwise
they need to put down 20 % Print the down payment"""

house_price = 1000000

good_credit = False

if good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2

print(f"Retail Price of House for you = ${down_payment}")
