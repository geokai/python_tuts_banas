# for loops and cycling through lists
for i in [2, 4, 6, 8, 10]:
    print('i =', i)
print()

for i in range(10):
    print("i =", i)
print()

for i in range(2, 10):
    print("i =", i)
print()

# floating point numbers
your_float = input("Enter a float: ")

your_float = float(your_float)

print("Round to 2 decimals : {:.2f}".format(your_float))


# order of operations
print("3 + 4 * 5 = {}".format(3 + 4 * 5))
print("(3 + 4) * 5 = {}".format((3 + 4) * 5))
print()


# the while loop
import random

rand_num = random.randrange(1, 51)  # generate a random value from 1 thru' 50

i = 1   # set the iterator

while (i != rand_num):      # declare the loop condition
    i += 1                  # increment the iterator

print("The random value is :", rand_num)
print()


i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break

    print("Odd :", i)

    i += 1
