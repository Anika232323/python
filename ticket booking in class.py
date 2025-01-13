import random
class Customer:
    def __init__(self,cust_id,name,phone):
        self.cust_id=cust_id
        self.name=name
        self.phone=phone
    def generate_customer_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"
    def verify_customer_id(cust_id):
        if cust_id[0:4]=="TICK" and cust_id[4:8].isdigit():
            print("valid")
        else:
            print("Invalid")

class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":1000,"seats":100},"Movie":{"price":150,"seats":200},"Drama":{"price":100,"seats":100}}
        self.booked_tickets=[]
    def view_events():
        for events,details in self.events.items():
            print(f"{events}: {details['price']} per ticket {details['seats']} available")
        
    def book_tickets(self,event_name,quantity,customer):
        if event_name in self.events:
            event=self.events[event_name]
            if event['seats']>=quantity:
                totalprice=event['price']*quantity
                event['seats']-=quantity
                self.booked_tickets.append({"Customer_id":Customer.cust_id,"Event":event_name,"Quantity":quantity,"Total price":totalprice})
            else:
                print("Seats are not available!!!!")
        else:
            print("Event is not available!!!")

    def view_tickets(self,customer):
        print("***********Ticket Information*************")
        cus_ticket=[t for t in self.booked_tickets if t["Customer_id"]==Customer.cust_id]
        if not cus_ticket:
            print("No tickets booked")
        else:
            for tick in cus_ticket:
                print(f"Event: {tick['event']}, Quantity: {tick['quantity']}, Total cost: {tick['totalprice']}")
                
if __name__=="__main__":
    book=TicketBooking()
    print("***********Welcome to TICKET Booking application*************")
    cust_id=input("Enter the customer id:")
    if Customer.verify_customer_id(cust_id):
        name=input("Enter name:")
        phone=int(input("Enter phone number:"))
        customer=Customer(cust_id,name,phone)
        print("********Booking Details**********")
    else:
        print("Invalid!!! Please register")
        name=input("Enter your name:")
        phone=int(input("Enter your phone:"))
        cust_id=Customer.generate_customer_id()
        customer=Customer(cust_id,name,phone)
        print("Your customer id is:",cust_id)
    while True:
        print("*************Booking Info****************")
        print("\n1.View Details")
        print("\n2.Book tickets")
        print("\n3.View my tickets")
        print("\n4.Exit")
        choice=int(input("Enter any option to continue booking:"))
        if choice==1:
            book.view_events()
        elif choice==2:
            event_name=input("Enter any event:")
            quantity=int(input("Enter the number of seats:"))
            book.book_tickets(event_name,quantity,customer)
        elif choice==3:
            book.view.tickets()
        elif choice==4:
            exit()
            
    
