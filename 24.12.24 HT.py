class Ecommerce:
    def __init__(self,base_price,discount_percentage=0,tax_percentage=0):
        self.base_price=base_price
        self.discount_percentage=discount_percentage
        self.tax_percentage=tax_percentage

    def calculate_final_price(self):
        if base_price<0 or discount_percentage<0 or tax_percentage<0:
            raise ValueError("Invalid amount")
        else:
            discount=((discount_percentage)/100)*base_price
            tax=((tax_percentage)/100)*base_price
            total=(base_price+tax)-discount
            return total

base_price=float(input("Enter the base price of the product:"))
discount_percentage=float(input("Enter the discount percentage:"))
tax_percentage=float(input("Enter the tax percentage:"))
try:
    com=Ecommerce(base_price,discount_percentage,tax_percentage)
    result=com.calculate_final_price()
    print(result)
except ValueError as e:
    print(e)
