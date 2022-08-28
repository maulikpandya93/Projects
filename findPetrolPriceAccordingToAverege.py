avg = float(input("HOW MUCH AVEREGE DOES YOUR CAR GIVE?\n"))
km = float(input("HOW MANY KILOMETER IS THE DISTANCE?\n"))
pp = float(input("PETROL PRICE:\n"))

a = km/avg
b = a*pp
print(f"THE PETROL PRICE WILL BE: {b}")

person = float(input("ENTER THE NUMBER OF PERSON TO DIVIDE: "))

c = b/person
print(f"PETROL PRICE PER PERSON WILL BE: {int(c)}")