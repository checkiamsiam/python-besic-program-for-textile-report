lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num % 2 == 0:
        print(num)
