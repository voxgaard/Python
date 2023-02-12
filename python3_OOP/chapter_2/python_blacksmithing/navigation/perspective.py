#Imports pending

#This is where the current game-state is printed and directed
class Agency:
    '''Process the player input and print properties'''
    def __init__(self):
        
        #These will offer the player decisions
        self.decisions = {
            "Travel": protagonist.action_travel(),
            "Review": protagonist.action_review(),
            "Vendor": protagonist.action_vendor(),
        }
        #These will offer the player destinations
        self.travel = {
            "Go to the Mine": locations.mine(),
            "Go to the Forge": locations.forge(),
            "Go to the Encampment": locations.camp()
        }
    def display_UI(self):
        '''Display possible actions.'''
        print("""
            1. Travel\n
            2. Review\n
            3. Vendor
            """)
    def display_travel(self):
        '''Display possible destinations.'''
        print("""
            1. Camp\n
            2. Mine\n
            3. Forge
            """)
    def display_review(self):
        '''Print dynamic character state'''
        print("""
            Your skill value is {0}.\n
            Your stamina value is {1}.\n
            You have {2} coins.\n
            Your inventory contains {3}.
            """.format(self.attributes("skill"), self.attributes("stamina"), self.attributes("coins"), self.attributes("inventory")))
    def display_sell(self):
        print(
            "Your wares sold for {0}".format(inventory.exchange_value)
            )
    def play(self):
        '''Display the UI and respond to choices.'''
        while True:
            self.display_UI()
            decision = input("Choose an action: ")
            action = self.decisions.get(decision)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(decision))