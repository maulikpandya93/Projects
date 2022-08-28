class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks
        
    def displayAvailableBooks(self):
        print("BOOKS PRESENT IN THIS LIBRARY ARE: ")
        for i,book in enumerate(self.books):
            print(f"\t{i+1} {book}")
            
    def borrowBook(self,bookName):
            if bookName in self.books:
                print(f"YOU HAVE BEEN ISSUED {bookName}. PLEASE KEEP IT SAFE AND RETURN IT IN 30 DAYS!! ")
                self.books.remove(bookName)
                return True
            else:
                print("SORRY! BOOK IS EITHER NOT AVAIALBLE OR ALREADY BEEN ISSUED TO SOMEONE ELSE. WAIT UNTIL THE BOOK IS RETURNED.")
                return False
            
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("THANK YOU FOR RETURNING THIS BOOK! HAVE A GREAT DAY.")
        
class Student:
        
    def requestBook(self):
        self.book = input("ENTER THE NAME OF THE BOOK YOU WANT TO BORROW: ")
        return self.book
        
    def returnBook(self):
        self.book = input("ENTER THE NAME OF THE BOOK YOU WANT TO RETURN: ")
        return self.book
        
        
if __name__ == "__main__":
    centralLibrary = Library(['ALGORITHMS','DJANGO','JAVA','C++','PYTHON'])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n
*****  WELCOME TO CENTRAL LIBRARY  *****
        Please choose an option:
          1-> LIST OF BOOKS
          2-> REQUEST A BOOK
          3-> ADD OR RETURN A BOOK
          4-> EXIT
        '''
        print(welcomeMsg)
        a = int(input("ENTER A CHOICE: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("THANKS FOR USING THIS LIBRARY. HAVE GREAT DAY!")
            exit()
        else:
            print("INVALID CHOICE!")
        
