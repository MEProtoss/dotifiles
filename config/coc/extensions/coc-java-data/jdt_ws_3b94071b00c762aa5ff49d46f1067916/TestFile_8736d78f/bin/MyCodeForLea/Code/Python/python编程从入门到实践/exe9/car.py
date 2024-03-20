""" A set of classes used to represent fuel powered vehicles and electric vehicles """

class Car:
    """ a simple attempt to Simulate car """

    def __init__(self,make,model,year):
        '''Initialize and describe the attributes of the car'''
        self.make = make 
        self.model = model 
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        """Return neat descriptive information"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a message indicating the mileage of the car"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        """Set the odometer to the specified value and prohibit it from being recalled"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """Increase the odometer reading by the specified amount"""
        self.odometer_reading += miles 


class Battery:
    """ a simple attempt to simulate battery of electric vehicles"""

    def __init__(self,battery_size=75):
        """Initialize the properties of the battery"""
        
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a message indicating the capacity of battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a message indicating the range of electric vehicles"""
        if self.battery_size==75:
            range = 260
        elif self.battery_size== 100:
            range=315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            
        print(f"This car's battery has been upgraded and the battery_size is {self.battery_size} now.")

class ElectricCar(Car):
    """The uniqueness of electric vehicles"""

    def __init__(self,make,model,year):
        """
        Initialize the properties of the parent class,and then Initialize the unique properties of electric vehicles
        """
        super().__init__(make,model,year)
        self.battery = Battery()
# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_description_name())

# # my_new_car.odometer_reading=23
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# my_used_car = Car('subaru','outback','2015')
# print(my_used_car.get_description_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

