class player:
    def __init__(self, name : str, health: int):
        self.name = name
        self.health = health
        self.inventory = Inventory(owner=self)

class Enemy:
    def __init__(self, name: str, health: int, AtackDamage: int):
        self.name = name
        self.health = health
        self.AtackDamage = AtackDamage
        self.Dead = False

    def SpawnEnemy(self):
        print(f"You have spawned the {self.name}!")

    def atack(self, player):
        if player.ifWeaponEquipped and self.health > 0:
            self.health = self.health - player.weapon.damage
            print(f"{player.name}! you did {player.weapon.damage} damage to the {self.name}!")
            self.health = self.health - player.weapon.damage
            print(f"{self.name} has done {self.AtackDamage} damage! -{self.AtackDamage}health")
            player.health = player.health - self.AtackDamage
        elif self.health <= 0:
            print(f"You have eliminated the {self.name}!")
        elif player.ifWeaponEquipped == False and self.health > 0:
            print("equip a weapon to attack!")
        elif player.ifWeaponEquiped and self.health < 0 and self.Dead == False:
            print(f"You have already eliminated the {self.name}!")
                
class Item:
    def __init__(self, name: str, type: callable, value: int, effect: str):
        self.name = name
        self.type = type
        self.value = value
        self.effect = effect
    
    def Description(self):
        print(f'The item {self.name} is of type {self.type}, has a value of {self.value}, and has the effect of "{self.effect}"')

class Weapon(Item):
    def __init__(self, name: str, value: int, damage: int):
        self.name = name
        self.value = value
        self.damage = damage
    
    def equipWeapon(self, Item):
        if Item.type == "weapon" and not self.ifWeaponEquipped:
            print(f"You have equipped the {Item.name}!")
            self.ifWeaponEquipped = True
        elif Item.type == "weapon" and self.ifWeaponEquipped:
            print("You already have a weapon equipped!")
        else:
            print("You can't equip that!")

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
    
    def __str__(self):
        inventory_str = f"""Inventory Items: {[item.name for item in self.items]}
player health: {self.owner.health}"""
        if self.ifWeaponEquipped:
            equipped_weapon = [item.name for item in self.items if item.type == 'weapon']
            if equipped_weapon:
                inventory_str += f"\nequipped weapon: {equipped_weapon[0]}"
        return inventory_str

class food(Item):
    def __init__(self, name: str, value: int, effect: int):
        self.name = name
        self.value = value
        self.effect = effect
    
    def eat(self, Item):
        if Item == food:
            print(f"you have eaten an {self.name}!")
            Inventory.RemoveItem(self)
            player.health += self.value

Vlen = player("Vlen", 100)
VlenInventory = Inventory(Vlen)
Sword =  Weapon("Sword", 10, "damage")