QUESTION 1:
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def displayVehicleInfo(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
class Car(Vehicle):
    def __init__(self,make,model,year,doors,trunkCapacity):
        Vehicle.__init__(self,make,model,year)
        self.doors=doors
        self.trunkCapacity=trunkCapacity
    def displayCarInfo(self):
        print("No. of doors:",self.doors)
        print("Car capacity:",self.trunkCapacity)
class Truck(Vehicle):
    def __init__(self,make,model,year,cargoCapacity,axle):
        Vehicle.__init__(self,make,model,year)
        self.cargoCapacity=cargoCapacity
        self.axle=axle
    def displayTruckInfo(self):
        print("Cargo Capacity:",self.cargoCapacity)
        print("Axles:",self.axle)
class PickupTruck(Car,Truck):
    def __init__(self,make,model,year,doors,trunkCapacity,cargoCapacity,axle):
        Car.__init__(self,make,model,year,doors,trunkCapacity)
        Truck.__init__(self,make,model,year,cargoCapacity,axle)
    def displayAll(self):
        self.displayVehicleInfo()
        self.displayCarInfo()
        self.displayTruckInfo()
m=PickupTruck("Toyota","Camry",2020,"4 doors","15.1 cubic feet","38.0 cubic feet",2)
m.displayAll()

QUESTION 2:
class Product:
    def __init__(self,Id,name,price):
        self.Id=Id
        self.name=name
        self.price=price
    def displayProduct(self):
        print("Product ID:",self.Id)
        print("Product name:",self.name)
        print("Product price:",self.price)
class Electronics(Product):
    def __init__(self,Id,name,price,warranty,brand):
        Product.__init__(self,Id,name,price)
        self.warranty=warranty
        self.brand=brand
    def displayElectronics(self):
        print("Warranty:",self.warranty)
        print("Brand:",self.brand)
class Clothing(Product):
    def __init__(self,Id,name,price,size,material):
        Product.__init__(self,Id,name,price)
        self.size=size
        self.material=material
    def displayClothing(self):
        print("Size:",self.size)
        print("Material:",self.material)
phone=Electronics(24536,"iPhone 15 Pro","1,34,900rs.","1-year","Apple")
shirt=Clothing(97535,"Croptop","345rs.","S","Cotton")
phone.displayProduct()
phone.displayElectronics()
shirt.displayProduct()
shirt.displayClothing()
