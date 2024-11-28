class Inventory:
    def __init__(self):
        self.prodId=234
        self.prodName="PhoneCase"
        self.prodCount=5
    def display(self):
        print(f"Product ID: {self.prodId}")
        print(f"Product Name: {self.prodName}")
        print(f"Product Count: {self.prodCount}")
Products=Inventory()
Products.display()
