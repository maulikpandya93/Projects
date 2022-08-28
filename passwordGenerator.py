import string
import random

s1 = string.ascii_lowercase
s2 = string.digits
s3 = string.punctuation
s4 = string.ascii_uppercase
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
user = input("ENTER THE LENGTH OF PASSWORD: ")
try:
    user = int(user)
    print("YOUR SECURED PASSWORD IS:")
    print("".join(random.sample(s,user)))
except:
    print("PLEASE ENTER THE NUMBER!")

