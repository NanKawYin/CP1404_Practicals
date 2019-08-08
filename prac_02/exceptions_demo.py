is_finished = False
while is_finished == False:

    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        is_finished = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

"""
1. When will a ValueError occur?
  Ans: When the user make and input other then integer ValueError will be occur.
2. When will a ZeroDivisionError occur?
  Ans: When the user put zero in denominator, ZeroDivisionError will be occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
  Ans: Yes."""
