import random

print("You can chose to throw a 4, 6 or 12 slided dice")
print('To exit enter 00')


def roll():
    four_slided_random_number = random.randint(1, 4)
    six_slided_random_number = random.randint(1, 6)
    twelve_slided_random_number = random.randint(1, 12)
    number1 = int(input("Enter number of dice: "))

    if number1 == 4:
        print("You rolled a",four_slided_random_number)

    elif number1 == 6:
        print("You rolled a",six_slided_random_number)

    elif number1 == 12:
        print("You rolled a",twelve_slided_random_number)

    elif number1 == str('00'):
        return

    else:
        print("You have to enter 4 ,6 or 12")
        return roll()


roll()
