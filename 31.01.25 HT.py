class Book_stall:
    def __init__(self,price,discount,discount_price):
        self.book_name=""
        self.cust_id=""
        self.price=price
        self.discount=0
        self.discount_price=0
    def validate_name(self,book_name):
        if book_name.isalpha()==True:
            return book_name
    def validate_id(self,cust_id):
        if int(cust_id)>=1:
            return cust_id
    def user_input(self):
        while True:
            book_name=input("Enter your Book Name:")
            if self.validate_name(book_name):
                self.book_name=book_name
                break
            print("Book name should be have only alphabets")

        while True:
            cust_id=input("Enter your Customer ID:")
            if self.validate_id(cust_id):
                self.cust_id=cust_id
                break
            print("Customer ID should be greater than or equal to 1")
    def calculate_discount(self):
        self.cust_id=int(self.cust_id)
        if 1<=self.cust_id<=100:
            self.discount=50
        elif 101<=self.cust_id<=300:
            self.discount=30
        elif 301<=self.cust_id<=400:
            self.discount=20
        elif 401<=self.cust_id<=500:
            self.discount=10
        else:
            self.discount=0
        self.discount_price=self.price-(self.price*(self.discount/100))

    def display(self):
        self.calculate_discount()
        print(f"Price of the Book is {self.price} MRP")
        print(f"You are eligible for Discounted of {self.discount}%")
        print(f"Your discounted Price for the Book is {self.discount_price} MRP")
while True:
    b=Book_stall(400,0,0)
    b.user_input()
    b.display()

    choice=input("Do you want to continue? (yes/no):").lower()
    if choice!="yes":
        break

    
