'''
Answer for Question 7 - PIAT: Improved Full Game.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
import name
import train
import shop
import game
import random
import setup
from mouse import Mouse
import sys

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
CHEESE_TYPES = ("cheddar", "marble", "swiss")

def run_setup():
    master= '/home/game_master/'
    timestamp = setup.time()
    abnormalities_detected = False
    verification_result = setup.verification(master, timestamp)
    abnormalities_detected = False

    # Using a while loop to check for abnormalities
    i = 0
    while not abnormalities_detected and i < len(verification_result):
        if verification_result[i] == "Abnormalities detected...":
            abnormalities_detected = True
        i += 1
    
    if abnormalities_detected:
        repair_choice = input("Do you want to repair the game? ").strip().lower()
        if repair_choice == "yes":
            installation_result = setup.installation(master, timestamp)
            print("Launching game...")
            print(".\n.\n.")
            return False  
        else:
            print("Game may malfunction and personalization will be locked.")
            proceed_choice = input("Are you sure you want to proceed? ").lower()
            if proceed_choice == "yes":
                print("You have been warned!!!")
                print("Launching game...")
                print(".\n.\n.")
                return True 
            else:
                sys.exit()
    else:
        print("Launching game...")
        print(".\n.\n.")
        return False  # Return False if there were no abnormalities detected

def personalisation(tampered_files):
    if tampered_files:  
        print("Welcome to the Kingdom, Hunter Bob!")
        return "Bob"

    hunter_name = input("What's ye name, Hunter? ")
    
    if name.is_valid_name(hunter_name) and not name.is_profanity(hunter_name):
        print("Welcome to the Kingdom, Hunter {}!".format(hunter_name))
        return hunter_name

    else:
        print("That's not nice!")
        print("I'll give ye 3 attempts to get it right or I'll name ye!")
        print("Let's try again...")
        n = 0
        while n < 3:
            hunter_name = input("What's ye name, Hunter? ")
            if name.is_valid_name(hunter_name) and not name.is_profanity(hunter_name):
                print(f"Welcome to the Kingdom, Hunter {hunter_name}!")
                return hunter_name
            else: 
                print(f"Nice try. Strike {n+1}!")
                n += 1          
    src = "/home/files/animals.txt"
    past = "/home/files/names.txt"
    print("I told ye to be nice!!!")
    hunter_name = name.generate_name(hunter_name, src, past)
    print(f"Welcome to the Kingdom, Hunter {hunter_name}!")
    return hunter_name

def get_benefit(cheese: str) -> str:
    '''
    This function takes the type of cheese as input and returns the benefits of the enchanted trap.
    Parameters:
        cheese: str, the type of cheese chosen by the player.
    Returns:
        benefits: str, a string representing the benefits of the enchanted trap.
    '''
    benefits = ""
    if cheese.lower() == "cheddar":
        benefits = "+25 points drop by next Brown mouse"
    elif cheese.lower() == "marble":
        benefits = "+25 gold drop by next Brown mouse"
    elif cheese.lower() == "swiss":
        benefits = "+0.25 attraction to Tiny mouse"
    else:
        benefits = "No benefits for this cheese."
    return benefits
    
def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
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

                # NEW: Display benefits if the trap is enchanted before asking for confirmation
                if e_flag:
                    benefits = get_benefit(cheese[i][0])  # Assuming get_benefit function exists
                    print(f"Your {trap} has a one-time enchantment granting {benefits}.")

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

def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int, trap: str, e_flag: bool) -> tuple:
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
                        mouse = Mouse(cheese=cheese_name.capitalize(), enchant=e_flag)
                        mouse_name = mouse.get_name()
                        if mouse_name is None:
                            print("Nothing happens.")
                            print(f"My gold: {gold}, My points: {points}\n")
                            failure += 1
                            e_flag = False
                        else:
                            print(f"Caught a {mouse_name} mouse!")
                            print(mouse.get_coat())
                            gold += mouse.get_gold()
                            points += mouse.get_points()
                            print(f"My gold: {gold}, My points: {points}\n")
                            failure = 0
                            e_flag = False  # reset the enchantment after a mouse has been caught
                        consume_cheese(cheese_name, cheese)
                        break
                    i += 1
                else:
                    print("Nothing happens. You are out of cheese!")
                    print(f"My gold: {gold}, My points: {points}\n")
                    failure += 1
                    e_flag = False
            else:
                print("Nothing happens. You are out of cheese!")
                print(f"My gold: {gold}, My points: {points}\n")
                failure += 1
                e_flag = False
        elif command == "stop hunt":
            e_flag = False
            repeat_game = False
        else:
            print("Do nothing.")
            print(f"My gold: {gold}, My points: {points}\n")
            failure += 1
            e_flag = False
        
        if failure == 5:
            failure = 0
            command = input("Do you want to continue to hunt? ").strip().lower()
            if command == "no":
                repeat_game = False
    e_flag = False
    return gold, points, e_flag



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

def has_cheese(to_check: str, my_cheese: list) -> int:
    '''
    Check if a cheese is present in the inventory and return its quantity
    Parameters:
        to_check: str, the type of cheese to check
        my_cheese: list, all the cheese and its quantities the player currently possesses
    Returns:
        int, quantity of the cheese in the inventory. Returns 0 if the cheese is not found in the inventory
    '''
    i = 0
    while i < len(my_cheese):
        if my_cheese[i][0].lower() == to_check.lower():
            return my_cheese[i][1]
        i += 1
    return 0

def main():
    tampered_files = run_setup()
    
    title: str = 'Mousehunt'
    logo: str = '       ____()()\n      /      @@\n`~~~~~\_;m__m._>o\n'
    credits: str = 'Inspired by Mousehunt© Hitgrab'
    author: str = 'Programmer - An INFO1110/COMP9001 Student'
    print(title + '\n')
    print(logo)
    print(credits)
    print(author)
    print('Mice art - Joan Stark and Hayley Jane Wakenshaw')
    print("")
    hunter_name = personalisation(tampered_files)

    print("Before we begin, let's train you up!")
    e_flag = False
    skip = input("Press \"Enter\" to start training or \"skip\" to Start Game: ").strip().lower()
    if skip.lower() != "skip":
        print("")
        trap = train.main() #underwent training 
        if trap == None:
            trap = "Cardboard and Hook Trap"
        elif trap == "High Strain Steel Trap" or "Hot Tub Trap":
            e_flag = True
    if e_flag:
        trap = f"One-time Enchanted {trap}"

    else: #no training
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

        while True:
            try:
                choice = float(input("Enter a number between 1 and 4: "))
                if choice < 1 or choice > 4:
                    print("Must be between 1 and 4.")
                    continue
                elif choice > 1 or choice < 4:
                    break
            except ValueError as e:
                print("Invalid input.")  # Display the error message
                continue

        if choice == 1:
            return None

        elif choice == 2:
            gold, points, e_flag = hunt(gold, cheese, trap_cheese, points, trap, e_flag)
            e_flag = False
            if e_flag == False:
                trap = trap.replace("One-time Enchanted ", "") # revert trap name back to original

        elif choice == 3:
            print("")
            gold = game.cheese_shop(gold, cheese, trap)

        elif choice == 4:
            print("")
            trap_status, trap_cheese = change_cheese(hunter_name, trap, cheese, e_flag)


if __name__ == '__main__':
    main()
