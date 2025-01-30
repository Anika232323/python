class Pizza_Size:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check(self,budget):
        if not isinstance(budget,(int,float)) or budget<0:
            raise ValueError("Budget canot be negative!!")
        return True
    def calc_balance(self,budget):
        return budget-self.price
    def suggest_size(self,budget):
        self.check(budget)
        try:
            
            if budget>self.price:
                print(f"You can buy {self.name} size")
                print(f"Your balance is {self.calc_balance(budget)}")
            elif budget==self.price:
                print(f"You can buy {self.name} size")
                print("No balance left")
            else:
                print("You cannot afford a pizza. Your budget is insufficient")
        except ValueError:
            print("Please enter a numerical value")
small=Pizza_Size("small",200)
medium=Pizza_Size("medium",300)
large=Pizza_Size("large",500)
sizes=[small,medium,large]
try:
    budget=float(input("Enter your budget:"))
    for i in sizes:
        i.suggest_size(budget)
except ValueError as e:
    print(e)
