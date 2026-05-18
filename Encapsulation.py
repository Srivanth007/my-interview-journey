class PiggyBank:
    def __init__(self):
        self.__money = 0 #The double underscore makes the variable private

    def insert_coin(self, amount):
        if amount > 0:
            self.__money += amount
            print(f"Inserted {amount} coins. Total: {self.__money} coins.")
        else:
            print("Please insert a positive amount of coins.")

    def check_balance(self):
        print(f"Current balance: {self.__money} coins.")

# Create a PiggyBank object
my_piggy_bank = PiggyBank()
my_piggy_bank.insert_coin(10)  # Insert coins
my_piggy_bank.check_balance()  # Check balance