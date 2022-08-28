from itertools import count
from math import factorial

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

def fact_TarilingZeros(num):
    count = 0
    i = 5
    while(num//i !=0):
        count += int(num/i)
        i *= 5
    return count

num = int(input("ENTER THE NUMBER TO FIND FACTORIAL(PLZ ENTER LOW NUMBER TO AVOID ERROR):\n"))
num1 = int(input("ENTER THE NUMBER TO FIND TRAILING ZEROS IN A FACTORIAL:\n"))

print(fact(num))
print(fact_TarilingZeros(num1))