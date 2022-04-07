import random

yes = ["yes", "Yes"]
no = ["no", "No"]


def end():
    more = input("Do you want more quotes? ")
    if more in yes:
        b = random.randint(1,21)
        text_file = open("\\School_system\\quotes.txt", "r")
        a = text_file.read().splitlines()
        print(a[b])
        text_file.close()
        
    elif more in no:
        print('Goodbye')
        return

    else:
        print("You have to say yes for me to print out a quote, if you don't want just say no")
        return end()


def start():

    choice = input("Do you want a quote:")

    if choice in yes:
        b = random.randint(1,21)
        text_file = open("\\School_system\\quotes.txt", "r")
        a = text_file.read().splitlines()
        print(a[b])
        text_file.close()
        return end()

    elif choice in no:
        print("Goodbye")
        return

    else:
        print("You have to say yes for me to print out a quote, if you don't want just say no")
        return start()


start()
