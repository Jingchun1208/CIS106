class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discounted_price(self):
        return self.sticker_price * 0.90  

    def display_info(self):
        return f"{self.make} {self.model} - Sticker Price: ${self.sticker_price:.2f}, Discounted Price: ${self.discounted_price():.2f}"

class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels_price = 1000.00
        self.sport_engine_price = 3000.00
        self.sport_interior_price = 2000.00

    def price_with_options(self, sport_wheels="N", sport_engine="N", sport_interior="N"):
        total_price = self.discounted_price()
        if sport_wheels.upper() == "Y":
            total_price += self.sport_wheels_price
        if sport_engine.upper() == "Y":
            total_price += self.sport_engine_price
        if sport_interior.upper() == "Y":
            total_price += self.sport_interior_price
        return total_price

    
    def display_info(self, sport_wheels="N", sport_engine="N", sport_interior="N"):
        return f"{self.make} {self.model} - Final Price with Options: ${self.price_with_options(sport_wheels, sport_engine, sport_interior):.2f}"


class Luxury(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.gps_price = 5000.00
        self.self_driving_price = 10000.00

    def price_with_options(self, gps="N", self_driving="N"):
        total_price = self.discounted_price()
        if gps.upper() == "Y":
            total_price += self.gps_price
        if self_driving.upper() == "Y":
            total_price += self.self_driving_price
        return total_price

    def display_info(self, gps="N", self_driving="N"):
        return f"{self.make} {self.model} - Final Price with Options: ${self.price_with_options(gps, self_driving):.2f}"


car1 = Car("Toyota", "Camry", 40000)
sport1 = Sport("Ford", "Mustang", 50000)
luxury1 = Luxury("Tesla", "Model S", 90000)

print(car1.display_info())  

print(sport1.display_info(sport_wheels="Y", sport_engine="N", sport_interior="Y"))  
print(sport1.display_info(sport_wheels="Y", sport_engine="Y", sport_interior="Y")) 

print(luxury1.display_info(gps="Y", self_driving="N"))  
print(luxury1.display_info(gps="Y", self_driving="Y"))  
