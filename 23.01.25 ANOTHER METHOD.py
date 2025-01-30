class HotelRoom:
    def  __init__(self):
        self.__room_number=None
        self.__is_occupied=False
        self.__rate_per_night=None
        
    def get_room_number(self):
        return self.__room_number
    def set_room_number(self,room_number):
        if isinstance(room_number,int)and room_number>0:
            self.__room_number=room_number
        else:
            raise ValueError("Room number must be a positive number")
     
    def get_rate_per_night(self):
        return self.__rate_per_night
    def set_rate_per_night(self,rate):
        if isinstance(rate,(int,float))and rate>0:
            self.__rate_per_night=rate
        else:
            raise ValueError("Rate per night must be greater than zero")

    def check_in(self):
        if self.__is_occupied:
            print("Room is already occupied.")
        else:
            self.__is_occupied=True
            print("Checked in successfully")

    def check_out(self):
        if not self.__is_occupied:
            print("Room is already vaccant.")
        else:
            self.__is_occupied=False
            print("Checked out successfully")

    def  display_details(self):
        occupied_status="Yes" if self.__is_occupied else "No"
        print(f"Room_number:{self.__room_number}\nRate per night:${self.__rate_per_night:.2f}\nOccupied:{occupied_status}")

room=HotelRoom()

try:
    room_number=int(input("Enter the room number: "))
    room.set_room_number(room_number)
except ValueError as e:
    print(f"Invalid Input:{e}")

try:
    rate=float(input("Enter the rate per night: "))
    room.set_rate_per_night(rate)
except ValueError as e:
    print(f"Invalid Input:{e}")

room.display_details()

while True:
    print("\nOptions:\n1.Check-in\n2.Check-out\n3.Display room details\n4.Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        room.check_in()
    elif choice=="2":
        room.check_out()
    elif choice=="3":
        room.display_details()
    elif choice=="4":
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Please try again.")
