class item:
    def __init__(self, name: str, type: str, value: int):
        self.name = name
        self.type = type

    def describe(self, type):
        if self.type == "weapon":
            print("this item is a weapon")
        elif self.type == "tool":
            print("this item is a tool")
        elif self.type == "food":
            print("this item is food")
        elif self.type == "material":
            print("this item is a material")
        elif self.type == "other":
            print("this item is miscellaneous")
        else:
            print("this item type is not valid")
    
class inventory:
    def __init__(self):
        self.items = []
    
    def AddItem(self, item, NumberOfItems: int):
        items = []
        for x in range(NumberOfItems):
            self.items.append(item)

    def RemoveItem(self, item: str):
        self.items.remove(item)

    def __str__(self):
        return f"Inventory items: {[item.name for item in self.items]}"

myInventory = inventory = inventory()