

a = input("Choose a calculator, you can either choose VAT, Tax or Times Tables:")
if a=="VAT":
    num1=int(input("Enter amount:"))
    Vat = 1.14*num1
    print("Your Vat is" ,Vat)

elif a=="TAX":
    num2 = float(input("Enter amount:"))
    Tax =(num2//100)*5400
    
    print("Your Tax is",Tax)

elif a=="Times Tables":
    table = int(input("Enter the number of the table: "))
    
    for counter in range(11):
        answer = table * counter
        print(table,"x",counter,"=",answer)

else:
    print("You response must match the three given options")
