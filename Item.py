from Enums import ItemType


class Item:

    def __init__(self, name='name', description='Description', quantity=0, itemType = ItemType.MISC):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.type = itemType

    def increaseQuantity (self, newValue):
        self.quantity += newValue