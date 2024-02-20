'''
Write your answer for the full OO version of the game here.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
from mouse import Mouse
from hunter import Hunter
from cshop import CheeseShop
from trap import Trap
from interface import Interface

class Game:
    def __init__(self):
        self.player = Hunter()
        self.interface = Interface(self.player)
        self.trap = Trap()
        self.gold = 125
        self.points = 0
        self.cheese = {"Cheddar": 0, "Marble": 0, "Swiss": 0}
        self.trap_cheese = None
        self.enchanted = False
        self.cheese_shop = CheeseShop()

    def run(self):
        while True:
            print("\nWhat do you want to do now, Hunter {}?".format(self.player.get_name()))
            print(self.interface.menu)
            try:
                choice = input()
                if not choice.isnumeric():
                    print("I did not understand.")
                    print("")
                    continue
                choice = int(choice)
                self.interface.move_to(choice)
            except EOFError:
                print("Invalid choice.")


if __name__ == "__main__":
    game = Game()
    game.run()
