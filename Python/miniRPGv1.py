class player:
    def __init__(self, name : str, health: int):
        self.name = name
        self.health = health
        self.inventory = Inventory(owner=self)
    
class Item:
    def __init__(self, name: str, type: str, value: int, effect: str):
        self.name = name
        self.type = type
        self.value = value
        self.effect = effect
    
    def Description(self):
        print(f'The item {self.name} is of type {self.type}, has a value of {self.value}, and has the effect of "{self.effect}"')
    
    def Eat(self, player):
        if self.type == "food":
            player.health = player.health + self.value
            print(f"You have eaten an apple! +{self.value} health!")
            player.inventory.RemoveItem(self, 1)
        else:
            print("You can't eat that!")
    
class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self.items = []
        self.ifWeaponEquipped = False
        
    def AddItem(self, Item, NumberOfItems):
        items = []
        for x in range(NumberOfItems):
            self.items.append(Item)
    
    def RemoveItem(self, Item, NumberOfItems):
        for x in range(NumberOfItems):
            self.items.remove(Item)
    
    def equipItem(self, Item):
        if Item.type == "weapon" and not self.ifWeaponEquipped:
            print(f"You have equipped the {Item.name}!")
            self.ifWeaponEquipped = True
        elif Item.type == "weapon" and self.ifWeaponEquipped:
            print("You already have a weapon equipped!")
        else:
            print("You can't equip that!")
    
    def __str__(self):
        inventory_str = f"""Inventory Items: {[item.name for item in self.items]}
player health: {self.owner.health}"""
        if self.ifWeaponEquipped:
            equipped_weapon = [item.name for item in self.items if item.type == 'weapon']
            if equipped_weapon:
                inventory_str += f"\nequipped weapon: {equipped_weapon[0]}"
        return inventory_str

Vlen = player("Vlen", 100)
VlenInventory = Inventory(Vlen)
Sword = Item("Sword", "weapon", -50, "10 damage")
Apple = Item("Apple", "food", 10, "+ 10 health")
Vlen.inventory.AddItem(Apple, 2)
Vlen.inventory.AddItem(Sword, 1)
Vlen.inventory.equipItem(Sword)
Vlen.inventory.equipItem(Sword)
Vlen.inventory.equipItem(Apple)
Apple.Description()
Sword.Description()
print(Vlen.inventory)
Apple.Eat(Vlen)
print(Vlen.inventory)