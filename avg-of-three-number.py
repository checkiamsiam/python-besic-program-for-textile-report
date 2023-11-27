def avg(num1, num2 , num3):
    average = (num1 + num2 + num3) / 3
    return average

# Get the three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average
average = avg(num1, num2, num3)
# Print the average
print("The average of the three numbers is:", average)
