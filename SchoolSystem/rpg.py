Usercharacter_1 = input("Please enter your character name:")
Usercharacter_2 = input("Please enter your character's attack:")
Usercharacter_3 = input("Please enter a defence capability for your character between 0 and 100:")
text_file = open("\\School_system\\RPG.txt", "a")
text_file.write("\nName:"+Usercharacter_1+"\n")
text_file.write("Attack:"+Usercharacter_2+"\n")
text_file.write("Defence capability:"+Usercharacter_3+"\n")
text_file.close()

print("File created")
choice=input("Do you want to see the data written(Y/N)")

lists = ["Yes","yes","Y","y","YES"]
if choice in lists:
    text_file = open("\\School_system\\RPG.txt", "r")
    while True:
        a = text_file.readline()
        if not a:
            break
        print(a)

else:
    print("Bye")


