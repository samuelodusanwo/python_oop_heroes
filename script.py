# Parent Class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name                # Public attribute
        self.power = power              # Public attribute
        self.city = city                # Public attribute
        self.__identity = "Secret"      # Private attribute (Encapsulation)
    
    def use_power(self):
        print(f"{self.name} uses {self.power} to protect {self.city}!")
    
    def get_identity(self):
        return f"{self.name}'s true identity is {self.__identity}"
    
    def set_identity(self, identity):
        self.__identity = identity


# Subclass: FlyingHero (Inheritance + Polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, city):
        super().__init__(name, "Flight", city)

    # Polymorphism: This method overrides the parent
    def use_power(self):
        print(f"{self.name} soars through the skies to save {self.city}!")

# Subclass: SpeedHero (Inheritance + Polymorphism)
class SpeedHero(Superhero):
    def __init__(self, name, city):
        super().__init__(name, "Super Speed", city)

    def use_power(self):
        print(f"{self.name} runs faster than lightning to save {self.city}!")

# --- Let's Create Objects ---
ironman = Superhero("Ironman", "Technology", "New York")
ironman.set_identity("Tony Stark")

falcon = FlyingHero("Falcon", "Washington D.C.")
flash = SpeedHero("Flash", "Central City")

# --- Test Their Powers ---
ironman.use_power()
print(ironman.get_identity())

falcon.use_power()
flash.use_power()


class Car:
    def __init__(self, model):
        self.model = model
        
    def move(self):
        print(f"{self.model} is moving")
        
class Plane(Car):
    def move(self):
        print(f"{self.model} plane moves so fast before taking off")
        

for tec in [Car("Toyota"), Plane("BMW")]:
    tec.move()