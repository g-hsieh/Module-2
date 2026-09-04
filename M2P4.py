print("Please enter your last name ")
lastName = input()
print("How many credits are you taking this semester? ")
credits = float(input())
tuition = 250 * credits
totalTuition = credits * 250 + 100
print("Your tuition in dollars is " + str(tuition))
print("Student with a last name of " + lastName)
print("Your total tuition with lab fee in dollars is " + str(totalTuition))
