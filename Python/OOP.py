# OOP programming
class MyClass:
    def __init__(self, type: str, perpose: str):
        self.type = type
        self.perpose = perpose

class Microwave:
    def __init__ (self, type: str, PowerRating: int):
        self.type = type
        self.PowerRating = PowerRating
        self.TurnedOn: bool = False

    def turn_on(self):
        if self.TurnedOn == True:
            print(f"{self.type} microwave is already on.")
        else:
            self.TurnedOn = True
            print(f"{self.type} microwave is now turned on.")

    def turn_off(self):
        if self.TurnedOn == False:
            print(f"{self.type} microwave is already off")
        else:
            self.TurnedOn = False
            print(f"{self.type} microwave is now off")
    
    def run(self, seconds: int):
        if self.TurnedOn:
            print(f"{self.type} microwave is now running for {seconds} seconds")
        else:
            print("turn on your microwave first")

gorenje: Microwave = Microwave(type = "Gorenje", PowerRating = 500)

gorenje.turn_on()
gorenje.run(5)
gorenje.turn_off()

bosch: Microwave = Microwave(type = "Bosch", PowerRating = 1000)

bosch.turn_on()
bosch.run(5)
bosch.turn_off()