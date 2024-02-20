'''
Write solutions to 3. New Mouse Release here.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''

'''
Keep this line!
'''
import random
from art import BROWN, FIELD, GREY, WHITE, TINY 

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")

# Mouse probabilities given cheese type and enchantment status
CHEESE_PROBABILITIES = {
    "Cheddar": (0.5, 0.1, 0.15, 0.1, 0.1, 0.05),
    "Marble": (0.6, 0.05, 0.2, 0.05, 0.02, 0.08),
    "Swiss": (0.7, 0.01, 0.05, 0.05, 0.04, 0.15),
}

COATS_OF_ARMS = {
    "Brown": BROWN,
    "Field": FIELD,
    "Grey": GREY,
    "White": WHITE,
    "Tiny": TINY,
}

def generate_mouse(cheese="Cheddar", enchant=False) -> str | None:
    '''
    Spawn a random mouse during a hunt depending on cheese type
    Returns:
        spawn_mouse: str | None, type of mouse
    '''
    probabilities = generate_probabilities(cheese, enchant)
    x = random.random()
    cumulative_probability = 0.0
    index = 0
    while index < len(TYPE_OF_MOUSE):
        cumulative_probability += probabilities[index]
        if x < cumulative_probability:
            return TYPE_OF_MOUSE[index]
        index += 1
    return None

def generate_probabilities(cheese_type, enchant=False):
    probabilities = list(CHEESE_PROBABILITIES.get(cheese_type, CHEESE_PROBABILITIES["Cheddar"]))
    if cheese_type == "Swiss" and enchant:
        probabilities[0] = 0.45 
        probabilities[-1] = 0.4        
    return tuple(probabilities)

def generate_coat(mouse_type):
    return COATS_OF_ARMS.get(mouse_type, "")

def loot_lut(mouse_type: str | None, cheese_type=None, enchant=False) -> tuple:
    '''
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
        cheese_type: str, type of cheese used
        enchant: bool, whether the trap was enchanted or not
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    '''
    # Initialize gold and points
    gold = 0
    points = 0

    # Assign gold and points based on mouse type
    if mouse_type is None:
        return gold, points
    elif mouse_type == "Brown":
        gold, points = 125, 115
    elif mouse_type == "Field":
        gold, points = 200, 200
    elif mouse_type == "Grey":
        gold, points = 125, 90
    elif mouse_type == "White":
        gold, points = 100, 70
    elif mouse_type == "Tiny":
        gold, points = 900, 200

    # Apply enchantment bonuses
    if enchant:
        if cheese_type == "Cheddar" and mouse_type == "Brown":
            points += 25
        elif cheese_type == "Marble" and mouse_type == "Brown":
            gold += 25

    return gold, points

class Mouse:
    def __init__(self, cheese="Cheddar", enchant=False):
        self.name = generate_mouse(cheese, enchant)
        self.gold, self.points = loot_lut(self.name, cheese, enchant)
        self.coat = generate_coat(self.name)

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def get_coat(self) -> str:
        return self.coat

    def __str__(self) -> str:
        return str(self.name) if self.name is not None else "None"

