def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert_fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
