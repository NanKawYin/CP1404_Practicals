for i in range(1, 21, 2):
    print(i, end=' ')
print()
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()
print()

count = int(input("Enter count: "))
for i in range(0, count, 1):
    print("*", end=' ')
print()
print()

count = int(input("Enter count: "))
for o in range(1, count+1, 1):
    for i in range(0, o, 1):
        print("*", end=' ')
    print()
print()
print()



MENU = """Negative Number - Quit"""
print(MENU)
sales = float(input("Enter sales: $"))
bonus = 0;
while sales >=0:
    if sales < 1000:
      bonus = sales * 0.1
    else:
        bouns = sales * 0.15
    print("Bonus: $ {}".format(bonus))
    print()
    print(MENU)
    sales= float (input ("Enter sales : $ "))
print("Thank you.")
print()
print()

