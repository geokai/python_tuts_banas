# Ask the user to input 2 values and store them in variables in num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()


# Convert the strings into regular numbers Integer
num1 = int(num1)
num2 = int(num2)


# Add the values and store in sumof
sumof = num1 + num2


# Subtract values and store in variable difference
difference = num1 - num2

# Multiply the values in variable product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2


# Use modulus in the values to find remainder
reminder = num1 % num2


# Print the results
print("{} + {} = {}".format(num1, num2, sumof))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {:.1f}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, reminder))
