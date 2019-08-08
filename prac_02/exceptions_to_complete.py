"""   finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        # TODO: this line
        pass
    except:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
"""
finished = False
result = 0
while not finished:
    try:
        num1 = int(input("Enter the number : "))
        num2 = int(input("Enter the number : "))
        pass
        result = num1 + num2
        finished = True
    except ValueError:
        print("Please enter a valid integer : ")
print("Valid result is:", result)

