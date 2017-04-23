# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their
# investment * interest
# Print out the earnings after a 10 year period

# Ask the user for the amount invested and for the interest rate
amount = input("Enter the amount to invest: ")
interest_rate = input("Interest Rate: ")

# Convert the value to a float
amount = float(amount)

# Convert value to a float and round the percentage rate to 2 digits
interest_rate = float(interest_rate) * 0.01


# Use a for loop to cycle through 10 years and range from 0 to 9
for i in range(1, 11):
    amount = amount + (amount * interest_rate)


# Output the results
    print("Amount at end of year {}, \t${:.2f}".format(i, amount))

print()
print("Investment after 10 years : ${:.2f}".format(amount))
