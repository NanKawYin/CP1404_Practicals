'''Example use:

Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75'''

Cents = float(input("Enter cents : "))
kWh = float(input("Enter kWh : "))
'''Electricity_Bill = float(input("Enter electricity bill estimator: "))'''
NumberOfDays = int(input("Enter number of days : "))
Estimated_bill = float(Cents*kWh*NumberOfDays*0.01)
print("Estimated bill is ${:.2f}".format(Estimated_bill))