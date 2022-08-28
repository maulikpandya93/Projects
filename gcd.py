from tkinter import Y


x = int(input("ENTER NUMBER 1:"))
y = int(input("ENTER NUMBER 2:"))
if x > y:
    t = y
else:
    t = x
for i in range(1,t+1):
    if((x % i == 0) and (y % i == 0)):
        gcd = i
print (f"THE GCD OF {x} AND {y} IS: {gcd}")