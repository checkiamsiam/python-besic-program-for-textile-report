# by type conversion

# num = int(input("Enter a number: "))

# numStr = str(num)

# count = len(numStr)

# print("Total digits:", count)


# by loop
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1  

# print("Total digits are", count)