#Imports pending

#Inventory to hold the protagonist's wares

class Wares:
#Need a method of generating Wares based on skill/location
    def __init__(self, title, value):
        self.title = title
        self.value = merchant.exchange_value(title)


class Inventory:
#An array of the currently possessed wares
    def __init__(self):
        self.wares = []
    def new_ware(self, skill, location, title):
        self.wares.append(Wares(title))
    def view_wares(self):
        return [wares for wares in self.wares]