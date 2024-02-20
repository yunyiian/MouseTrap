'''
Write your solution for the class Interface here.
This is your answer for Question 8.4.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
from mouse import Mouse
from hunter import Hunter
from cshop import CheeseShop
from trap import Trap
import game_final
CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
class Interface:
    def __init__(self, player: Hunter = Hunter()):
        self._player = player

    @property
    def menu(self):
        menu = {
            1: "Exit game",
            2: "Join the Hunt",
            3: "The Cheese Shop",
            4: "Change Cheese",
        }
        menu_str = ''
        index = 1
        while index <= len(menu):
            menu_str += f"{index}. {menu[index]}\n"
            index += 1
        return menu_str

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if not isinstance(value, Hunter):
            raise ValueError("Player must be an instance of Hunter.")
        self._player = value


    def change_cheese(self):
        repeat_change = True
        while repeat_change:
            print(f"Hunter {self._player.name}, you currently have:")
            i = 0
            while i < len(self._player.cheese):
                cheese_type, quantity = self._player.cheese[i]
                print(f"{cheese_type} - {quantity}")
                i += 1
            print("")
            cheese_name = input("Type cheese name to arm trap: ").strip().lower()

            if cheese_name == "back":
                return False, None

            valid_cheeses = ['cheddar', 'swiss', 'marble']
            valid_cheese_present = False
            i = 0
            while i < len(valid_cheeses):
                if valid_cheeses[i] == cheese_name:
                    valid_cheese_present = True
                    break
                i += 1

            if not valid_cheese_present:
                print("No such cheese!\n")
                continue

            i = 0
            while i < len(self._player.cheese):
                cheese_type, quantity = self._player.cheese[i]
                if cheese_type.lower() == cheese_name and quantity > 0:
                    if self._player.trap.one_time_enchantment:
                        benefits = self._player.trap.get_benefit(cheese_type)
                        print(f"Your One-time Enchanted {self._player.trap.get_trap_name()} has a one-time enchantment granting {benefits}.")

                    confirm = input(f"Do you want to arm your trap with {cheese_type}? ").strip().lower()

                    if confirm == "yes":
                        print(f"{str(self._player.trap)} is now armed with {cheese_type}!")
                        self._player.arm_trap(cheese_type)
                        self._player.consume_cheese(cheese_type)
                        return True, cheese_type
                    elif confirm == "no":
                        print("")
                        break
                    elif confirm == "back":
                        return False, None
                    else:
                        print("Invalid input. Please enter either 'yes' or 'no'.")
                i += 1
            else:
                print("Out of cheese!\n")

    def cheese_shop(self):
        shop = CheeseShop()
        shop.move_to(self.player)

    def hunt(self):
        gold = self.player.gold
        cheese = self.player.cheese
        trap_cheese = self.player.trap.get_trap_cheese()
        points = self.player.points
        trap = str(self.player.trap)
        e_flag = self.player.trap.get_one_time_enchantment()

        gold, points, e_flag = self._hunt(gold, cheese, trap_cheese, points, trap, e_flag)

        self.player.gold = gold
        self.player.points = points
        self.player.trap.set_one_time_enchantment(e_flag)

    def _hunt(self, gold: int, cheese: list, trap_cheese: str | None, points: int, trap: str, e_flag: bool) -> tuple:
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
                            self.player.consume_cheese(cheese_name)
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

    @property
    def menu_keys(self):
        menu = {
            1: "Exit game",
            2: "Join the Hunt",
            3: "The Cheese Shop",
            4: "Change Cheese",
        }
        return list(menu.keys())

    def move_to(self, choice):
        if isinstance(choice, int):
            keys = self.menu_keys
            index = 0
            found = False
            while index < len(keys):
                if choice == keys[index]:
                    found = True
                    break
                index += 1
            if found:
                if choice == 1:
                    exit(0)
                elif choice == 2:
                    self.hunt()
                elif choice == 3:
                    print("Welcome to The Cheese Shop!")
                    index = 0
                    while index < len(CHEESE_MENU):
                        cheese_class, price = CHEESE_MENU[index]
                        print("{} - {} gold".format(cheese_class.capitalize(), price))
                        index += 1
                    print("")
                    self.cheese_shop()
                elif choice == 4:
                    self.change_cheese()
            else:
                print("Must be within 1 and 4.")
        else:
            print("Invalid input. Try again!")

