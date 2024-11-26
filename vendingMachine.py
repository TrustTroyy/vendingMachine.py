class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.50),
            Beverage("Water", 1.00),
            Beverage("Juice", 2.00),
            Beverage("Tea", 1.25),
            Beverage("Coffee", 1.75),
        ]

    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        for i, beverage in enumerate(self.beverages, start=1):
            print(f"{i}. {beverage.name} - ${beverage.price:.2f}")
        print("0. Exit")

    def select_beverage(self, choice):
        if 1 <= choice <= len(self.beverages):
            return self.beverages[choice - 1]
        else:
            return None

    def process_payment(self, beverage, money):
        if money >= beverage.price:
            change = money - beverage.price
            return True, change
        else:
            return False, beverage.price - money

    def vend(self, beverage):
        print(f"Vending {beverage.name}... Enjoy your drink!")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nSelect a beverage by number (or 0 to exit): "))
                if choice == 0:
                    print("Thank you for using the vending machine. Goodbye!")
                    break
                beverage = self.select_beverage(choice)
                if not beverage:
                    print("Invalid selection. Please try again.")
                    continue

                print(f"You selected {beverage.name}, which costs ${beverage.price:.2f}.")
                money = float(input("Insert money: $"))
                success, result = self.process_payment(beverage, money)

                if success:
                    print(f"Payment successful. Your change is ${result:.2f}.")
                    self.vend(beverage)
                else:
                    print(f"Insufficient funds. Please add ${result:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

machine = VendingMachine()
machine.run()
