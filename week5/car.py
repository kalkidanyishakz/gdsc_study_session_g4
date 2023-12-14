class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity=battery_capacity
        self.charge=0
    
    def charge(self, charge_amount):
        if self.charge+charge_amount>=self.battery_capacity:
            self.charge=self.battery_capacity
        else:
            self.charge+=charge_amount
        
    def display_info(self):
        super().display_info()
        print(f'battery capacity: {self.battery_capacity}')
        print(f'charge: {self.charge}')

            


my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info()

my_car2 = ElectricCar("Toyota", "Corolla", 2022, 200)
my_car2.display_info()

