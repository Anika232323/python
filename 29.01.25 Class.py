class Maggi_Pack:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check(self,budget):
        if  not isinstance(budget,(int,float)) or budget<0:
            raise ValueError("Budget should be in int or float and should not be negative")
        return True
    def calculate_budget(self,budget):
        return budget-self.price
    def suggest_packet(self,budget):
        try:
            self.check(budget)
            if budget>self.price:
                print(f"You can buy the {self.name} pack")
                print(f"Your remaining balance is {self.calculate_budget(budget)}")
            elif budget==self.price:
                print(f"You can buy the {self.name} pack. No balance is remaining")
            else: 
                print(f"You will not be able to afford it. You will need {budget-self.price} to buy this pack")    
        except ValueError as ve:
            print(ve)
small=Maggi_Pack("sm  all",20)
regular=Maggi_Pack("regular",30)
big=Maggi_Pack("big",50)
packets=[big,regular,small]
try:
    budget=float(input("What is your budget:"))
    for i in packets:
        i.suggest_packet(budget)
except ValueError as e:
    print(e)
