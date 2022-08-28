num = int(input("NUM1: "))
num1 = int(input("NUM2: "))
num2 = int(input("NUM3: "))
for  i in range(1,11):
    print(f"|{num} X {i} = {num*i}|",end="\t|")
    print(f"{num1} X {i} = {num1*i}|",end="\t|")
    print(f"{num2} X {i} = {num2*i}|")
    