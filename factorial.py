def fact_num(n):
 fact = 1
 if n == 0 or n == 1:
    print(f"THE FACTORIAL OF {n} IS: 1")
 else:
  for i in range(1,n+1):    
    fact = fact * i
  print(f"THE FACTORIAL OF {n} IS: {fact}")
  
n = int(input("ENTER THE NUMBER: "))
fact_num(n)

