class CreditCardPayment:
    def pay(self,amount):
        return f"Paid {amount} using creditcard"
class PayPalPayment:
    def pay(self,amount):
        return f"Paid {amount} using PayPal"
class DebitCardPayment:
    def pay(self,amount):
        return f"Paid {amount} using debitcard"
class payment:
    def show(self,amount): #it has method as show so it gives error
        return f"Paid {amount}"
def process_payment(payment_method,amount):
    print(payment_method.pay(amount))

cc=CreditCardPayment()
process_payment(cc,200)

pp=PayPalPayment()
process_payment(pp,300)

dd=DebitCardPayment()
process_payment(dd,400)

#this shows error
'''p=payment()
process_payment(p,400)'''
