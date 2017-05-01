while True:
    try:
        number = int(input("Please enter a number : "))
        #print("The number you entered is {}".format(number))
        print()
        break

    except ValueError:
        print("You didn't enter a number")

    except:
        print("An unknow error occurred")

print("Thank you for entering a number")
print("You entered the number {}".format(number))
