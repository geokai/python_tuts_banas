# Problem: receive miles and convert to kilometers
# Ask the user to input miles and assign it to the variable

miles = input("Enter number of miles to convert: ")

# convert string to integer
miles = int(miles)

# Kilometers = miles * 1.60934
# perform calculation by multiplying miles by 1.60934
kilometers = miles * 0.62137

# Enter Miles 5
# 5 miles = 8.04 kilometers
# print results using format()
print("{} miles equals {:.2f} kilometers".format(miles, kilometers))
