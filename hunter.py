'''
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
import name
from trap import Trap

class Hunter:
    def __init__(self, name='Bob', gold=125, points=0, trap=None):
        self.name = name
        self.cheese = [['Cheddar', 0], ['Marble', 0], ['Swiss', 0]]
        self.trap = trap if trap else Trap(trap_name="")
        self.gold = gold
        self.points = points

    def set_name(self, player_name):
        if name.is_valid_name(player_name) and not name.is_profanity(player_name):
            self.name = player_name

    def set_cheese(self, cheese_quantities):
        if isinstance(cheese_quantities, tuple) and len(cheese_quantities) == 3:
            self.cheese[0][1] = cheese_quantities[0]
            self.cheese[1][1] = cheese_quantities[1]
            self.cheese[2][1] = cheese_quantities[2]

    def set_gold(self, gold_quantity):
        if isinstance(gold_quantity, int):
            self.gold = gold_quantity

    def set_points(self, point_quantity):
        if isinstance(point_quantity, int):
            self.points = point_quantity

    def get_name(self):
        return self.name

    def get_cheese(self):
        return "{} - {}\n{} - {}\n{} - {}".format(self.cheese[0][0], self.cheese[0][1], self.cheese[1][0], self.cheese[1][1], self.cheese[2][0], self.cheese[2][1])

    def get_gold(self):
        return self.gold

    def get_points(self):
        return self.points

    def update_cheese(self, cheese_quantities):
        if isinstance(cheese_quantities, tuple) and len(cheese_quantities) == 3:
            self.cheese[0][1] += cheese_quantities[0]
            self.cheese[1][1] += cheese_quantities[1]
            self.cheese[2][1] += cheese_quantities[2]

    def consume_cheese(self, cheese_type):
        if self.cheese[0][0].lower() == cheese_type.lower() and self.cheese[0][1] > 0:
            self.cheese[0][1] -= 1
        elif self.cheese[1][0].lower() == cheese_type.lower() and self.cheese[1][1] > 0:
            self.cheese[1][1] -= 1
        elif self.cheese[2][0].lower() == cheese_type.lower() and self.cheese[2][1] > 0:
            self.cheese[2][1] -= 1

    def have_cheese(self, cheese_type='Cheddar'):
        if not isinstance(cheese_type, str):
            cheese_type = str(cheese_type)
        if self.cheese[0][0].lower() == cheese_type.lower():
            return self.cheese[0][1]
        elif self.cheese[1][0].lower() == cheese_type.lower():
            return self.cheese[1][1]
        elif self.cheese[2][0].lower() == cheese_type.lower():
            return self.cheese[2][1]
        return 0

    def display_inventory(self):
        output = ["Gold - {}".format(self.gold)]
        output.append("{} - {}".format(self.cheese[0][0], self.cheese[0][1]))
        output.append("{} - {}".format(self.cheese[1][0], self.cheese[1][1]))
        output.append("{} - {}".format(self.cheese[2][0], self.cheese[2][1]))
        trap_info = "Trap - "
        if self.trap:
            if self.trap.get_one_time_enchantment():
                trap_info += "One-time Enchanted "
            trap_info += self.trap.get_trap_name()
        else:
            trap_info += "None"
        output.append(trap_info)
        return '\n'.join(output)

    def arm_trap(self, cheese_type):
        if self.have_cheese(cheese_type) > 0:
            self.trap.set_trap_cheese(cheese_type)
            self.trap.set_arm_status()
        else:
            self.trap.set_trap_cheese(None)
            self.trap.set_arm_status()

    def update_points(self, point_quantity):
        if isinstance(point_quantity, int):
            self.points += point_quantity

    def __str__(self):
        output = "Hunter {}".format(self.name)
        output += "\n" + self.display_inventory()
        return output

    def update_gold(self, gold_quantity):
        if isinstance(gold_quantity, int):
            self.gold += gold_quantity


