#Locations for the player to use the travel function to interact with
class Locations:
    def __init__(self):
        '''Locations to be displayed as options for the player'''
        self.locations = ["Mine", "Forge", "Camp", "Prison"]
    def enter_mine(self):
        '''A fuction for the mine'''
        print("You approach the mine.")
    def enter_forge(self):
        '''A fuction for the forge'''
        print("You approach the forge.")
    def enter_camp(self):
        '''A fuction for the camp'''
        print("You approach the camp.")
    def enter_mine(self):
        '''A fuction for the prison'''
        print("You've been thrown into prison.")