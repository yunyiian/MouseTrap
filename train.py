'''
Answer for Question 5 - The Training Again from Assignment 1.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''

import q4

def main():
    q4.intro()
    to_camp = q4.travel_to_camp()
    if to_camp == '\x1b':
        return None

    repeat = True
    while repeat:
        cheddar, trap = q4.setup_trap()
        if cheddar == '\x1b':
            return None
        
        horn_input = q4.sound_horn()
        if horn_input == '\x1b':
            return None

        hunt_status = q4.basic_hunt(cheddar, horn_input)
        success = hunt_status
        if success:
            q4.end(hunt_status, cheddar, horn_input)
        gold = 125
        print("")
        repeat_game = input("Press Enter to continue training and \"no\" to stop training: ").strip().lower()
        if repeat_game.lower() == "no":
            repeat = False
        elif repeat_game == '\x1b':
            repeat = False
        else:
            repeat = True
    return trap


if __name__ == '__main__':
    main()
