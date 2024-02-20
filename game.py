'''
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
import name
import train
import shop

# you can make more functions or global read-only variables here if you please!
def cheese_shop(gold, cheese, trap):
    print("Welcome to The Cheese Shop!")
    index = 0
    while index < len(CHEESE_MENU):
        cheese_class, price = CHEESE_MENU[index]
        print("{} - {} gold".format(cheese_class.capitalize(), price))
        index += 1
    repeat_shop = True
    while repeat_shop:
        menu = shop.intro_shop()
        if menu == "1":
            gold_spent, cheese_bought = shop.buy_cheese(gold)
            gold -= gold_spent
            i = 0
            while i < len(cheese_bought):
                cheese[i][1] += cheese_bought[i]
                i += 1
        elif menu == "2":
            shop.display_inventory(gold, cheese, trap)
        elif menu == "3":
            repeat_shop = False
        else:
            print("I did not understand.")
    
    return gold

def get_game_menu():
    '''
    Returns a string displaying all possible actions at the game menu.
    '''
    menu = "1. Exit game\n"
    menu += "2. Join the Hunt\n"
    menu += "3. The Cheese Shop\n"
    menu += "4. Change Cheese"
    return menu

def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    '''
    Handles the inputs and ouputs of the change cheese feature.
    Parameters:
        hunter_name: str,        the name of the player.
        trap:        str,        the trap name.
        cheese:      list,       all the cheese and its quantities the player 
                                 currently possesses.
        e_flag:      bool,       if the trap is enchanted, this will be True. 
                                 default value is False.
    Returns:
        trap_status: bool,       True if armed and False otherwise.
        trap_cheese: str | None, the type of cheese in the trap. if player 
                                 exits the function without arming 
                                 trap succesfully, this value is None.
    '''

    repeat_change = True
    while repeat_change:
        print(f"Hunter {hunter_name}, you currently have:")
        i = 0
        while i < len(cheese):
            cheese_type, quantity = cheese[i]
            print("{} - {}".format(cheese_type, quantity))
            i += 1
        print("")
        cheese_name = input("Type cheese name to arm trap: ").strip().lower()

        if cheese_name == "back":
            return False, None

        i = 0
        while i < len(CHEESE_TYPES):
            if CHEESE_TYPES[i] == cheese_name:
                break
            i += 1
        else:
            print("No such cheese!")
            print("")
            continue

        i = 0
        while i < len(cheese):
            if cheese[i][0].lower() == cheese_name and cheese[i][1] > 0:
                confirm = input(f"Do you want to arm your trap with {cheese[i][0]}? ").strip().lower()

                if confirm == "yes":
                    print(f"{trap} is now armed with {cheese[i][0]}!")
                    return True, cheese[i][0]
                elif confirm == "no":
                    print("")
                    break
                elif confirm == "back":
                    return False, None
                else:
                    print("Invalid input. Please enter either 'yes' or 'no'.")
            i += 1
        else:
            print("Out of cheese!")
            print("")


def consume_cheese(to_eat: str, cheese: list) -> None:
    '''
    Handles the consumption of cheese.
    Will modify the cheese list, if required.
    Parameters:
        to_eat:    str,        the type of cheese to consume during the hunt.
        cheese:    list,       all the cheeses and quantities the player 
                               currently possesses.
    '''
    index = 0
    while index < len(cheese):
        if cheese[index][0].lower() == to_eat.lower():
            cheese[index][1] -= 1
            break
        index += 1

def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of 
    the hunt, the gold and points earned, and whether users want to continue 
    after failing consecutively.
    The function will modify the cheese list, if required.
    Parameters:
        gold:        int,        the quantity of gold the player possesses.
        cheese:      list,       all the cheese and quantities the player 
                                 currently possesses.
        trap_cheese: str | None, the type of cheese that the trap is currently 
                                 armed with. if it's not armed, the value is None.
        points:      int,        the quantity of points that the player 
                                 currently possesses.
    Returns:
        gold:        int,        the updated quantity of gold after the hunt.   
        points:      int,        the updated quantity of points after the hunt.
    '''
    failure = 0
    repeat_game = True
    
    while repeat_game:
        print("Sound the horn to call for the mouse...")
        
        command = input("Sound the horn by typing \"yes\": ").strip().lower()
        
        if command == "yes":
            if trap_cheese is not None:
                cheese_name = trap_cheese.lower()
                i = 0
                while i < len(cheese):
                    if cheese[i][0].lower() == cheese_name and cheese[i][1] > 0:
                        if random.random() > 0.5:
                            print("Nothing happens.")
                            print(f"My gold: {gold}, My points: {points}\n")
                            failure += 1
                        else:
                            gold += 125
                            points += 115
                            print("Caught a Brown mouse!")
                            print(f"My gold: {gold}, My points: {points}\n")
                            failure = 0
                        consume_cheese(cheese_name, cheese)
                        break
                    i += 1
                else:
                    print("Nothing happens. You are out of cheese!")
                    print(f"My gold: {gold}, My points: {points}\n")
                    failure += 1
            else:
                print("Nothing happens. You are out of cheese!")
                print(f"My gold: {gold}, My points: {points}\n")
                failure += 1
        elif command == "stop hunt":
            repeat_game = False
        else:
            print("Do nothing.")
            print(f"My gold: {gold}, My points: {points}\n")
            failure += 1
        
        if failure == 5:
            failure = 0
            command = input("Do you want to continue to hunt? ").strip().lower()
            if command == "no":
                repeat_game = False
    return gold, points


CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
CHEESE_TYPES = ("cheddar", "marble", "swiss")

def main():
    '''
    Implement your code here.
    '''
    title: str = 'Mousehunt'
    logo: str = '       ____()()\n      /      @@\n`~~~~~\_;m__m._>o\n'
    credits: str = 'Inspired by Mousehunt© Hitgrab'
    author: str = 'Programmer - An INFO1110/COMP9001 Student'
    print(title + '\n')
    print(logo)
    print(credits)
    print(author)
    print('Mice art - Joan Stark')
    print("")
    print("What's ye name, Hunter?")
    hunter_name = input()
    
    if name.is_valid_name(hunter_name) == True:
        print("Welcome to the Kingdom, Hunter {}!".format(hunter_name))
    else:
        hunter_name = "Bob"
        print("Welcome to the Kingdom, Hunter {}!".format(hunter_name))

    print("Before we begin, let's train you up!")
    skip = input("Press \"Enter\" to start training or \"skip\" to Start Game: ").strip().lower()
    if skip.lower() != "skip":
        print("")
        trap = train.main()
        if trap == None:
            trap = "Cardboard and Hook Trap"
    else:
        trap = "Cardboard and Hook Trap"
    points = 0 
    gold = 125
    trap_cheese = None
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]

    repeat = True
    while repeat:
        print("\nWhat do ye want to do now, Hunter {}?".format(hunter_name))
        print("1. Exit game")
        print("2. Join the Hunt")
        print("3. The Cheese Shop")
        print("4. Change Cheese")
        choice = input()

        if choice == "1":
            repeat = False

        elif choice == "2":
            gold, points = hunt(gold, cheese, trap_cheese, points)

        elif choice == "3":
            gold = cheese_shop(gold, cheese, trap)

        elif choice == "4":
            e_flag = False
            trap_status, trap_cheese = change_cheese(hunter_name, trap, cheese, e_flag)
            if trap_status == True:
                e_flag = True


if __name__ == '__main__':
    main()
