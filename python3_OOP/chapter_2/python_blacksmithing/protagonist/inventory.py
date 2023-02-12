#Inventory to hold the protagonist's wares

class Wares:
    def __init__(self, title, value):
        self.title = title
        self.value = merchant.exchange_value(title)


class Inventory:
    def __init__(self):
        self.wares = []
    def new_ware(self, skill, location, title):
        self.wares.append(Wares(title))