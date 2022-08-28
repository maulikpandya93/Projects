class Calc:
    def __init__(self):
        print("***** WELCOME TO THE INDIAN KIRANA STORE *****")
    def totalSum(self):
        l = []
        k = []
        sum = 0
        print("PRESS T FOR TOTAL!")
        while(True):
            try:
                name = input("ITEM NAME: ")
                user = input("ENTER PRICE OF THE ITEM IN RUPEES: ")
                
               
                if user == "t" or name == "t":
                    break
                else:
                   l.append(name) 
                   k.append(user)
                    
                   user = int(user)
                   sum += user    
            except:
                print("PLEASE ENTER THE PRICE IN NUMBERS(NOT BLANK OR SENTENCE OR WORD)!")
        print(f"YOUR ITEMS AND ITS PRICES(in Rs) ARE {l}:{k}") 
        print(f"YOUR BILL TOTAL IS: {sum} Rs")
        
        
m = Calc()
print("***************")
m.totalSum()
print("THANKS FOR VISITING :)")


