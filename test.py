'''
Write solutions to 4. New Mouse Release here.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
"side effect for inputs and replace the inputs"

def test_mouse_class(n=10000):
    cheese_types = ["Cheddar", "Marble", "Swiss"]
    enchant_types = [True, False]

    i = 0
    while i < len(cheese_types):
        cheese = cheese_types[i]
        j = 0
        while j < len(enchant_types):
            enchant = enchant_types[j]

            mouse_counts = {}
            m = 0
            while m < len(TYPE_OF_MOUSE):
                mouse_type = TYPE_OF_MOUSE[m]
                mouse_counts[mouse_type] = 0
                m += 1
            
            k = 0
            while k < n:
                mouse = Mouse(cheese, enchant)
                mouse_counts[mouse.get_name()] += 1
                k += 1

            print(f"\nCheese type: {cheese}, Enchantment: {enchant}")
            l = 0
            while l < len(TYPE_OF_MOUSE):
                mouse_type = TYPE_OF_MOUSE[l]
                actual_probability = mouse_counts[mouse_type] / n
                expected_probability = generate_probabilities(cheese, enchant)[l]
                print(f"Mouse type: {mouse_type}, Actual probability: {actual_probability:.2f}, Expected probability: {expected_probability:.2f}")
                l += 1

            j += 1
        i += 1

if __name__ == "__main__":
    test_mouse_class()



'''
import unittest
from unittest.mock import patch

CHEESE_TYPES = ["cheddar", "marble", "swiss"]
CHEESE_MENU = [("cheddar", 10), ("marble", 15), ("swiss", 20)]

# Test cases for buy_cheese function
class TestBuyCheese(unittest.TestCase):
    @patch('builtins.input', side_effect=['swiss 3', 'back'])
    def test_buy_cheese_insufficient_gold(self, input):
        with self.assertRaises(SystemExit):
            gold_spent, bought_cheese = buy_cheese(30)

    @patch('builtins.input', side_effect=['marble -2', 'back'])
    def test_buy_cheese_negative_amount(self, input):
        with self.assertRaises(SystemExit):
            gold_spent, bought_cheese = buy_cheese(50)

    @patch('builtins.input', side_effect=['cheddar 3', 'back'])
    def test_buy_cheese_multiple_same_type(self, input):
        gold_spent, bought_cheese = buy_cheese(50)
        self.assertEqual((gold_spent, bought_cheese), (30, (3, 0, 0)))

# Test cases for change_cheese function
class TestChangeCheese(unittest.TestCase):
    @patch('builtins.input', side_effect=['cheddar', 'yes'])
    def test_arm_trap_available_cheese(self, input):
        trap_status, trap_cheese = change_cheese("Hunter", "Trap", [("cheddar", 2)])
        self.assertEqual((trap_status, trap_cheese), (True, "cheddar"))

    @patch('builtins.input', return_value='rock')
    def test_invalid_cheese_name(self, input):
        with self.assertRaises(SystemExit):
            trap_status, trap_cheese = change_cheese("Hunter", "Trap", [("cheddar", 2)])

    @patch('builtins.input', side_effect=['cheddar', 'back'])
    def test_back_after_enter_cheese_name(self, input):
        trap_status, trap_cheese = change_cheese("Hunter", "Trap", [("cheddar", 2)])
        self.assertEqual((trap_status, trap_cheese), (False, None))

if __name__ == '__main__':
    unittest.main()
'''


