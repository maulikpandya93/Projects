print("ENTER YOUR INTEGERS TO FIND AVG AND PRODUCT OF INTEGERS.")
num = int(input("HOW MANY INTEGERS YOU WANT TO ENTER? "))
s = 0
pro = 1
for i in range(1,num+1):
    
    n = int(input(f"INTEGER {i}: "))
    # q = input("PRESS q TO QUIT")
    s = s + n
    avg = s/n
    pro = pro * n
    
print(f"THE AVERAGE OF THESE INTEGERS IS: {avg}")
print(f"THE PRODUCT OF THESE INTEGERS IS: {pro}")
