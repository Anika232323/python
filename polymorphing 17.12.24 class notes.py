#polymorphism with inheritence
#using method overriding polymorphism allows us to define method in the child class that have the same name as the methods in the parent classs
#This process of re_implementing the inherited method in the child class is known as Method Overriding .
class Library:
    def issue_book(self,book_name,user):
        return f"Book issued: {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned is: {book_name} by {user}"
class DigitalLibrary(Library):
    def issue_book(self,book_name,user):
        return f"Book issued: {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned is: {book_name} by {user}"
lib=Library()
dig=DigitalLibrary()
book=input("Enter book name:")
username=input("Enter username:")
print(lib.issue_book(book,username))
print(lib.return_book(book,username))
print(dig.issue_book(book,username))
print(dig.return_book(book,username))
