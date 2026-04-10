class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"
    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
    def has_resources(self, water, milk, beans):
        if self.water < water:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return False
        if self.beans < beans:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return False
        return True
    def buy(self, choice):
        if choice == "1":
            if self.has_resources(250, 0, 16):
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
        elif choice == "2":  # latte
            if self.has_resources(350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
        elif choice == "3":
            if self.has_resources(200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0
    def process(self, user_input):
        if self.state == "action":
            if user_input == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.state = "buy"
            elif user_input == "fill":
                self.fill()
            elif user_input == "take":
                self.take()
            elif user_input == "remaining":
                self.print_state()
            elif user_input == "exit":
                return False
        elif self.state == "buy":
            if user_input == "back":
                self.state = "action"
            else:
                self.buy(user_input)
                self.state = "action"
        return True
machine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if not machine.process(action):
        break