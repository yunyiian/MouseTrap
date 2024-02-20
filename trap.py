'''
Write your solution for the class Trap here.
This is your answer for Question 8.1.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''


class Trap:
    VALID_TRAPS = ["Cardboard and Hook Trap", "High Strain Steel Trap", "Hot Tub Trap"]
    VALID_CHEESES = ["Cheddar", "Marble", "Swiss"]

    def __init__(self, trap_name=None, trap_cheese=None, arm_status=False, one_time_enchantment=False):
        self.trap_name = trap_name if trap_name is not None else ''
        self.trap_cheese = trap_cheese 
        self.arm_status = arm_status
        self.one_time_enchantment = one_time_enchantment

    def set_trap_name(self, name):
        if self.VALID_TRAPS.count(name) > 0:
            self.trap_name = name

    def set_trap_cheese(self, cheese):
        if cheese is None or self.VALID_CHEESES.count(cheese) > 0:
            self.trap_cheese = cheese

    def set_arm_status(self):
        if self.VALID_CHEESES.count(self.trap_cheese) > 0 and self.VALID_TRAPS.count(self.trap_name) > 0:
            self.arm_status = True
        else:
            self.arm_status = False

    def set_one_time_enchantment(self, status):
        if self.trap_name != "Cardboard and Hook Trap":
            self.one_time_enchantment = status

    def get_trap_name(self):
        return self.trap_name

    def get_trap_cheese(self):
        return self.trap_cheese

    def get_arm_status(self):
        return self.arm_status

    def get_one_time_enchantment(self):
        return self.one_time_enchantment

    @staticmethod
    def get_benefit(cheese: str) -> str:
        benefits = {
            "Cheddar": "+25 points drop by next Brown mouse",
            "Marble": "+25 gold drop by next Brown mouse",
            "Swiss": "+0.25 attraction to Tiny mouse"
        }
        return benefits.get(cheese, "No benefits for this cheese.")

    def __str__(self):
        if self.one_time_enchantment:
            return f"One-time Enchanted {self.trap_name}"
        else:
            return self.trap_name

