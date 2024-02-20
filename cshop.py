'''
Write your solution for the class CheeseShop here.
This is your answer for Question 8.3.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
import hunter

CHEESE_TYPES = ['cheddar', 'marble', 'swiss']
CHEESE_MENU = [['cheddar', 10], ['marble', 50], ['swiss', 100]]

class CheeseShop:
    def __init__(self):
        self.cheeses = {"Cheddar": 10, "Marble": 50, "Swiss": 100}
        self.menu = {1: "Buy cheese", 2: "View inventory", 3: "Leave shop"}

    def get_cheeses(self):
        cheese_list = []
        i = 0
        keys = list(self.cheeses.keys())
        while i < len(self.cheeses):
            cheese_list.append(f"{keys[i]} - {self.cheeses[keys[i]]} gold")
            i += 1
        return "\n".join(cheese_list)

    def get_menu(self):
        menu_list = []
        i = 1
        while i <= len(self.menu):
            menu_list.append(f"{i}. {self.menu[i]}")
            i += 1
        return "\n".join(menu_list)

    def greet(self):
        greeting = "Welcome to The Cheese Shop!\n" + self.get_cheeses()
        return greeting

    def buy_cheese(self, gold):
        bought_cheese = {"Cheddar": 0, "Marble": 0, "Swiss": 0}
        gold_spent = 0

        print("You have {} gold to spend.".format(gold))

        while True:
            purchase = input("State [cheese quantity]: ").capitalize()
            if purchase == "Back":
                return gold, tuple(bought_cheese.values())
            
            if self.cheeses.get(purchase.split()[0]) is None:
                print("We don't sell {}!".format(purchase.lower().split()[0]))
                print("You have {} gold to spend.".format(gold))
                continue
            
            cheese_type, quantity = purchase.split()
            if not quantity.isdigit():
                print("Invalid quantity.")
                print("You have {} gold to spend.".format(gold))
                continue
            quantity = int(quantity)

            if quantity <= 0:
                print("Must purchase positive amount of cheese.")
                print("You have {} gold to spend.".format(gold))
                continue

            cheese_price = self.cheeses.get(cheese_type)
            if gold < cheese_price * quantity:
                print("Insufficient gold.")
                print("You have {} gold to spend.".format(gold))
                continue

            gold_spent += cheese_price * quantity
            bought_cheese[cheese_type] += quantity
            gold -= cheese_price * quantity
            print("Successfully purchase {} {}.".format(quantity, cheese_type.lower()))
            print("You have {} gold to spend.".format(gold))


    def move_to(self, hunter):
        while True:
            print("How can I help ye?")
            print(self.get_menu())
            try:
                choice = input()
                if choice == "0":
                    raise ValueError('Invalid choice')
                    break
                elif not choice.isnumeric():
                    print("I did not understand.")
                    print("")
                    continue
                choice = int(choice)
                if choice < 1 or choice > 3:
                    raise ValueError('Invalid choice')
                    break
            except EOFError:
                raise ValueError('Invalid choice')
                break
            else:
                if choice == 1:
                    hunter.gold, cheese_bought = self.buy_cheese(hunter.gold)
                    i = 0
                    while i < len(cheese_bought):
                        hunter.cheese[i][1] += cheese_bought[i]
                        i += 1
                    print("")
                    continue
                elif choice == 2:
                    print(hunter.display_inventory())
                    print("")
                    continue
                elif choice == 3:
                    break


