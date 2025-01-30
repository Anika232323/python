class HotelRoom:
    def __init__(self):
        self.__room_num=int(input())
        self.__is_occupied=1
        self.__rate_per_night=float(input())
    def set_room_num(self):
        if self.__room_num>0:
            return "Valid"
        else:
            return "Invalid"
    def get_room_num(self):
        if self.set_room_num()=="Valid":
            return self.__room_num
        else:
            return "Room number should be a positive integer"
    def set_rate_per_night(self):
        if self.__rate_per_night>0:
            return "Valid"
        else:
            return "Invalid"
    def get_rate_per_night(self):
        if self.set_rate_per_night()=="Valid":
            return self.__rate_per_night
        else:
            return "Rate should be a greater than zero"
    def check_in(self):
        if self.__is_occupied==0:
            return "Occupied: No"
        else:
            raise ValueError("Room is already occupied")
    def check_out(self):
        if self.__is_occupied==1:
            return "Occupied: Yes"
        else:
            raise ValueError("Room is already vacant")
    def display_details(self):
        print(f"Room number: {self.get_room_num()}")
        print(f"Rate per night: {self.get_rate_per_night()}")
        print(self.check_in())
        
       
try:
    room = HotelRoom()
    room.display_details()
except ValueError as v:
    print(v)
try:
    room = HotelRoom()
    room.display_details()
except ValueError as e:
    print(e)
