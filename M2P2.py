print("Please enter your last name ")
lastName = input()
print("How many hours did you work?")
hours = float(input())
print("What is your hourly rate?")
rate = float(input())
grossPay = hours * rate
print("Your Gross Pay is a total amount of $" + str(grossPay))
print("with a Last Name of " + lastName)
