print("PATTERN NO: 1")
for i in range(6):
     print("*" * i)

print("\n")

print("PATTERN NO: 2")
for j in range(3):
     print(" " * (2-j), "*" * ((2 * j)+1))
for k in range(2,0,-1):
   if k==1:
       print(" " * (2), "*" * ((2 * k)-1))
   if k==2:        print(" " * (1), "*" * ((2 * k)-1))

print("\n")    

print("PATTERN NO: 3")
def star(n):
     for i in range(0,n+1):
      print ("* " * i)

n = 5
star(n)

print("\n")

print("PATTERN NO: 4")
for i in range(6):
     print("*  " * i)

print("\n")

print("PATTERN NO: 5")
def starp(n):
 k = n
 for i in range(1,n+1):
    for j in range(k):
        print(end=" ")
    
    k = k-1
    
    print("*" * i)  
    
num = 5 
starp(num)

print("\n")

print("PATTERN NO: 6")
def starTri(n):
 k = n
 for i in range(1,n+1):
    for j in range(1,k+1):
        print(end=" ")  
    
    k = k - 1
    print("* " * i)     
  
num1 = 5
starTri(num1)   

print("\n")

print("PATTERN NO: 7")

def starn(n):
 for i in range(1,n+1):
    k = 1
    for j in range(1,i+1):
        print(k,end=" ")
        k = k +1
    print("\n", end="")
    
num2 = 5
starn(num2)

print("\n")

print("PATTERN NO: 8")

def starn1(n):
 k =1
 for i in range(1,n+1):

    for j in range(1,i+1):
        print(k,end=" ")
        k = k +1
    print("\n", end="")
    
num2 = 5
starn1(num2)

print("\n")

print("PATTERN NO: 9")

def starnalpha(n):
 k = 65
 for i in range(1,n+1):

    for j in range(1,i+1):
        ch = chr(k)
        print(ch,end=" ")
        k = k +1
    print("\n", end="")
    
num2 = 5
starnalpha(num2)

print("\n")

print("PATTERN NO: 10")

def starnalpha1(n):

 for i in range(1,n+1):
    k = 65
    for j in range(1,i+1):
        ch = chr(k)
        print(ch,end=" ")
        k = k +1
    print("\n", end="")
    
num2 = 5
starnalpha1(num2)

print("\n")

print("PATTERN NO: 11")

def printNo(n):
 k = 3
 for i in range(1,n):
    for j in range(1,i):
        print(end=" ")
    print("10" * k,end="")
    print("1")
    k = k -1

num = 5
printNo(num)

print("\n")
    
print("PATTERN NO: 12")
rows = 5
for i in range(0,rows):
    for j in range(0,rows):
        print("* ",end="")
    print("\r")
print("\n")

print("PATTERN NO: 13")
rows = 5

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j," ",end="")
    print("\r")

print("\n")
    
print("PATTERN NO: 14")
rows = 5
for i in range(0,rows):
    for j in range(rows,i,-1):
        print("* ",end="")
    print("\r")

print("\n")

print("PATTERN NO: 15")
m = 0
rows = 9
for i in range(0,rows):
    if i >= 5:
        for j in range(rows-5,m,-1):
            print("* ",end="") 
        m = m+ 1 
        print("\r")
    else:
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
print("\n")

    