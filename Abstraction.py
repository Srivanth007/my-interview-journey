class coffeeMachine:
    def press_brew_button(self):
        self.__boil_water()
        self.__grind_beans()
        self.__pour_coffee()
        print("Your coffee is ready!")

    def __boil_water(self):
        print("Boiling water...")
    def __grind_beans(self):
        print("Grinding coffee beans...")
    def __pour_coffee(self):
        print("Pouring coffee into the cup...")

# Create a coffee machine object
my_coffee_machine = coffeeMachine()
my_coffee_machine.press_brew_button()  # Brew a cup of coffee
