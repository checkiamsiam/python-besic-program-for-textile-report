lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
sum = 0

for num in range(lower, upper + 1):
    if num % 2 != 0:
        sum += num

print("The sum of odd numbers is", sum)