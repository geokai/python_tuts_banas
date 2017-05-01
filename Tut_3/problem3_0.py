# Guess a number between 1 and 10 : 1  wrong
# Guess a number between 1 qnd 10 : 7
# You guessed it

# Create a secret number and assign to a variable
secret_number = 7

# begin the while loop
while True:
    guess = 0
    try:
        # Ask the user to guess the number and assign to a variable
        guess = int(input("Guess the number, 1-10 : "))

    except ValueError:
        print("Please enter only numbers 1-10")

        # Compare guess with secret number:
        # if the same tell the user they are right and break out of loop
    if secret_number == guess:
        print("You guessed correctly!")
        print("Good Bye")
        break

    # if not the same loops goes around again and asks the user to guess again
