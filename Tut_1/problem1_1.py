# If age is 5 Go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater than 17 say go to college
# Try to complete with 10 or less lines

# Ask user for their age
age = eval(input("Enter your age: "))


# Check age in conditional for age group and determine result
# Print result
if age == 5:
    print("Go to kindergarten")
elif (age >= 6) and (age <= 17):
    print("Go to grade {}".format(age - 5))
elif age > 17:
    print("Go to college")
else:
    print("Too young for school")