class player:
    def __init__(self, name : str, health: int, inventory: list):
        self.name = name
        self.health = health
        self.inventory = inventory
    
class Item:
    def __init__(self, name: str, type: str, value: int, effect: str):
        self.name = name
        self.type = type
        self.value = value
        self.effect = effect
    
    def Description(self):
        print(f'The item {self.name} is of type {self.type}, has a value of {self.value}, and has the effect of "{self.effect}"')
    
    def Eat(self):
        if self.type == "food":
            player.health = player.health + self.value
            print(f"You have eaten an apple! +{self.value} health!")
            self.RemoveItem(self, 1)
    
class Inventory:
    def __init__(self):
        self.items = []
        
    def AddItem(self, Item, NumberOfItems):
        items = []
        for x in range(NumberOfItems):
            self.items.append(Item)
    
    def RemoveItem(self, Item, NumberOfItems):
        for x in range(NumberOfItems):
            self.items.remove(Item)
    
    def __str__(self):
        return f"""Inventory Items: {[item.name for item in self.items]}
    player health: {player.health}"""

Vlen = player = player("Vlen", 100, [])
VlenInventory = Inventory = Inventory()
Sword = Item("Sword", "weapon", -50, "10 damage")
Apple = Item("Apple", "food", 10, "+ 10 health")
VlenInventory.AddItem(Apple, 2)
VlenInventory.AddItem(Sword, 1)
Apple.Description()
Sword.Description()
print(VlenInventory)
Apple.Eat()
print(VlenInventory)