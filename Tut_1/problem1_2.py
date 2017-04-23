# Convert a distance form mile to km and visa verda
# The user should input a distance number followed by either 'm' or 'km'

# create a default instruction and error message function
def guide_error():
    print("Enter a distance followed by 'm' or 'km' eg: 5 m / 7 km")

# print an initial instructional message
#print()
#guide_error()
#print()

# Ask the user for the distance and the units of that distance
# convert the distance to an integer
distance, unit = input("Enter the distance and Unit: ").split()

distance = int(distance)
k_units = 'kilometers'
m_units = 'miles'

# check if the user has entered miles or kilometers
if unit == 'm':
    kilometers = distance * 1.60934
    print("{} {} equals {:.2f} {}".format(distance, m_units, kilometers, k_units))
elif unit == 'km':
    miles = distance * 0.62137
    print("{} {} equals {:.2f} {}".format(distance, k_units, miles, m_units))

# make the relevant calculation
# and print the result
# print error message if incorrect input
else:
    guide_error()
