"""Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92  """

number_of_items = int(input("Enter Number of items: "))
amount = 0
result = 0
for i in range(0, number_of_items, 1):
    item_price = float(input("Enter Price of Items: $"))
    amount += item_price

if amount >100:
    result = amount-(amount * 0.1)
else:
    result = amount
print("Total Price for {} items is ${:.2F}".format(number_of_items,result))
print()
