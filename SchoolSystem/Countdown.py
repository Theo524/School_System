import time
counter = int(input("Welcome, this is a countdown timer, enter the amount of time you want to count:"))
for counter in range(counter, -1, -1):
    time.sleep(1)
    print(counter)

print("Blast off!")



