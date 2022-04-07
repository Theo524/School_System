print("Welcome,I will print the odd numbers you write, for you too see them sorted")
odd=[]
even=[]
for i in range(0,10):
    num = int(input("Enter any number:"))
    if num % 2 == 0:
        even.append(num)
        
    else:
        odd.append(num)
        odd.sort()

print(odd)
print(f'This were the even numbers: {even}')
