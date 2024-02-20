'''
Answer for Question 4 - The Training

Name: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975

'''
def intro():
    return print("Larry: I'm Larry. I'll be your hunting instructor.")

def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    to_camp = input("Press Enter to travel to the Meadow...")
    if to_camp == '\x1b':
        return to_camp
    else:
        print("Travelling to the Meadow...")
        print("Larry: This is your camp. Here you'll set up your mouse trap.")
    
def setup_trap() -> tuple:
    left_trap = "High Strain Steel Trap"
    right_trap = "Hot Tub Trap"
    no_trap = "Cardboard and Hook Trap"
    
    print("Larry: Let's get your first trap...")
    cheddar = input("Press Enter to view traps that Larry is holding...")
    trap = None
    if cheddar == '\x1b':
        return cheddar, trap
    else:
        print("Larry is holding...")
        print("Left: High Strain Steel Trap")
        print("Right: Hot Tub Trap")

        command = input('Select a trap by typing "left" or "right": ').strip().lower()
        if command == '\x1b':
            cheddar = command
            trap = no_trap

        elif command == "left":
            print("Larry: Excellent choice.")
            print("Your \"{}\" is now set!".format(left_trap))
            print("Larry: You need cheese to attract a mouse.")
            print("Larry places one cheddar on the trap!")
            cheddar = 1
            trap = left_trap

        elif command == "right":
            print("Larry: Excellent choice.")
            print("Your \"{}\" is now set!".format(right_trap))
            print("Larry: You need cheese to attract a mouse.")
            print("Larry places one cheddar on the trap!")
            cheddar = 1
            trap = right_trap
            
        else:
            print("Invalid command! No trap selected.")
            print("Larry: Odds are slim with no trap!")
            trap = no_trap
            cheddar = 0

        return cheddar, trap

def sound_horn() -> str:
    print("Sound the horn to call for the mouse...")
    horn_input = input('Sound the horn by typing "yes": ').strip().lower()
    return horn_input

def basic_hunt(cheddar: int, horn_input: str) -> bool:  
    if cheddar == 0 and horn_input != 'yes':
        print("Nothing happens.")
        return False

    elif cheddar == 1 and horn_input == 'yes':
        print('Caught a Brown mouse!')
        print("Congratulations. Ye have completed the training.")
        return True

    else:
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!")
        return False


def end(hunt_status: bool, cheddar: int, horn_input: str):
    if cheddar == 1 and horn_input == 'yes':
        return print("Good luck~")
    

def main():
    intro()
    travel_to_camp()
    cheddar, trap = setup_trap()
    horn_input = sound_horn()
    basic_hunt_result = basic_hunt(cheddar, horn_input)
    end(basic_hunt_result, cheddar, horn_input)

    

'''
This statement is true if you run this script.
This statement is false if this file is to be imported from another script. 
'''
if __name__ == '__main__':
    main()

