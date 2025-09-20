  # WEEK 5 ASSIGNMENT

# ASSIGNMENT 1: SMARTPHONE CLASS

# Parent class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    # methods
    def make_call(self, number):
        return f"Calling {number} from {self.model}..."
    
    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        return f"Battery charged to {self.battery}%"
    
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.model}..."
    
    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}% battery"

# Child class (inherits from Smartphone)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery, strap_colour):
        super().__init__(brand, model, storage, battery)
        self.strap_colour = strap_colour 
    
    # overriding a method (polymorphism)
    def make_call(self, number):
        return f"Calling {number} from your Smartwatch ({self.model})..."

# ASSIGNMENT 2: POLYMORPHISM CHALLENGE

class Vehicle:
    def move(self):
        return "The vehicle is moving."
        
class Car(Vehicle):
    def move(self):
        return "Driving on the road."
        
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky."
        
class Boat(Vehicle):
    def move(self):
        return "Sailing in the water."
    

# Testing both assignments


if __name__ == "__main__": 
    # --- Assignment 1 Test ---
    print("=== Assignment 1: Smartphone Class ===")
    phone1 = Smartphone("Samsung", "Galaxy S23", 256, 75)
    print(phone1)
    print(phone1.make_call("080 12345678"))
    print(phone1.charge(20))
    print(phone1.install_app("WhatsApp"))

    watch1 = Smartwatch("Apple", "Watch Series 9", 32, 50, "Black")
    print(watch1)
    print(watch1.make_call("08123456789"))

    # --- Assignment 2 Test ---
    print("\n=== Assignment 2: Polymorphism Challenge ===")
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(v.move())                      