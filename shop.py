'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
CHEESE_TYPES = ("cheddar", "marble", "swiss")

def intro_shop():
    print('')
    print("How can I help ye?")
    print("1. Buy cheese")
    print("2. View inventory")
    print("3. Leave shop")
    menu = input().strip().lower()
    return menu

def buy_cheese(gold: int) -> tuple:
    bought_cheese = {"cheddar": 0, "marble": 0, "swiss": 0}
    gold_spent = 0

    print("You have {} gold to spend.".format(gold))

    while True:
        purchase = input("State [cheese quantity]: ").lower()
        if purchase == "back":
            return gold_spent, tuple(bought_cheese.values())

        start_cheese = False
        i = 0
        while i < len(CHEESE_TYPES):
            if purchase.startswith(CHEESE_TYPES[i]):
                start_cheese = True
                break
            i += 1

        if not start_cheese:
            print("We don't sell {}!".format(purchase.split()[0]))
            print("You have {} gold to spend.".format(gold))
            continue

        purchase_words = purchase.split()
        if len(purchase_words) != 2:
            print("Missing quantity.")
            print("You have {} gold to spend.".format(gold))
            continue

        cheese_type, quantity = purchase_words
        if not quantity.isdigit():
            print("Invalid quantity.")
            print("You have {} gold to spend.".format(gold))
            continue
        quantity = int(quantity)

        if quantity <= 0:
            print("Must purchase positive amount of cheese.")
            print("You have {} gold to spend.".format(gold))
            continue
            
        cheese_price = CHEESE_MENU[i][1]
        
        if gold < cheese_price * quantity:
            print("Insufficient gold.")
            print("You have {} gold to spend.".format(gold))
            continue

        gold_spent += cheese_price * quantity
        bought_cheese[cheese_type] += quantity
        gold -= cheese_price * quantity
        print("Successfully purchase {} {}.".format(quantity, cheese_type))
        print("You have {} gold to spend.".format(gold))

def display_inventory(gold: int, cheese: list, trap: str):
    print("Gold - {}".format(gold))
    i = 0
    while i < len(cheese):
        cheese_type, quantity = cheese[i]
        print("{} - {}".format(cheese_type, quantity))
        i += 1
    print("Trap - {}".format(trap))

def main():
    print("Welcome to The Cheese Shop!")
    index = 0
    while index < len(CHEESE_MENU):
        cheese_class, price = CHEESE_MENU[index]
        print("{} - {} gold".format(cheese_class.capitalize(), price))
        index += 1
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'

    repeat = True
    while repeat:
        menu = intro_shop()
        if menu == "1":
            gold_spent, cheese_bought = buy_cheese(gold)
            gold -= gold_spent
            i = 0
            while i < len(cheese_bought):
                cheese[i][1] += cheese_bought[i]
                i += 1

        elif menu == "2":
            display_inventory(gold, cheese, trap)
        elif menu == "3":
            repeat = False

if __name__ == "__main__":
    main()

