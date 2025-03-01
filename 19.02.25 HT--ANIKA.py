class PaymentMethod:
    def pay(self, amt):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amt):
        print(f"Paid {amt} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amt):
        print(f"Paid {amt} using PayPal.")

class UPI(PaymentMethod):
    def pay(self, amt):
        print(f"Paid {amt} using UPI")

payment_methods = [CreditCard(), PayPal(), UPI()]
amt = int(input("Enter the amount: "))

for method in payment_methods:
    method.pay(amt)
