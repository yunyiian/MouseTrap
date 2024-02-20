'''
Answer for Question 5. Kids' Friendly.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''

# you can make more functions or global read-only variables here if you please!

'''
This part should be your solution from Assignment 1, 3. Functions.
'''

def is_valid_name(word: str) -> bool:
    length = len(word)
    int(length)
    a = length >= 0
    b = length <= 9
    is_valid_length: bool = a and b

    if len(word) > 0: 
        first_character = word[0]
        is_valid_start: bool = first_character.isalpha()
    else:
        is_valid_start = False

    space: str = ' ' or '_'
    is_one_word: bool = word.find(space) == -1


    is_valid_name = is_one_word and is_valid_start and is_valid_length
    return is_valid_name

import os

def is_profanity(word: str, database='/home/files/list.txt', records='/home/files/history.txt') -> bool:
    '''
    Checks if `word` is listed in the blacklist `database`.
    Parameters:
        word:     str,  word to check against database.
        database: str,  absolute directory to file containing list of bad words.
        records:  str,  absolute directory to file to record past offenses by player.
    Returns:
        result:   bool, status of check.
    '''
    try:
        with open(database, 'r') as db_file:
            blacklist = db_file.read().splitlines()
            word_found = False
            i = 0
            while not word_found and i < len(blacklist):
                if word == blacklist[i]:
                    word_found = True
                i += 1

            if word_found:
                if os.path.exists(records):
                    with open(records, 'a') as records_file:
                        records_file.write(f'{word}\n')
                else:
                    with open(records, 'w') as records_file:
                        records_file.write(f'{word}\n')
                return True
            else:
                return False
    except FileNotFoundError:
        print("Check directory of database!")
        return False


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag: bool = True) -> int:
    '''
    Count the occurrences of `word` contained in file_records.
    Parameters:
        word:         str,  target word to count number of occurrences.
        file_records: str,  absolute directory to file that contains past records.
        start_flag:   bool, set to False to count whole words. True to count words 
                            that start with.
    Returns:
        count:        int, total number of times `word` is found in the file.
    '''
    if not isinstance(word, str):
        print("First argument must be a string object!")
        return 0
    elif len(word) == 0:
        print("Must have at least one character in the string!")
        return 0

    try:
        with open(file_records, 'r') as file:
            data = file.read().lower()
            count = 0
            i = 0

            while i < len(data):
                line_start = i
                while i < len(data) and data[i] != '\n':
                    i += 1
                line_end = i
                line = data[line_start:line_end]
                i += 1
                
                if start_flag:
                    if line.lower().startswith(word.lower()[0]):
                        count += 1
                else:
                    if line.lower() == word.lower():
                        count += 1

        with open(file_records, 'a') as file:
            file.write(f'{word}\n')  

        return count
    except FileNotFoundError:
        print("File records not found!")
        return 0



def generate_name(word: str, src="/home/files/animals.txt", past="/home/files/names.txt") -> str:
    if not word:
        print("Must have at least one character in the string!")
        return "Bob"

    if not isinstance(word, str):
        print("First argument must be a string object!")
        return "Bob"

    try:
        with open(src, 'r') as src_file:
            names = src_file.readlines()
            i = 0
            while i < len(names):
                names[i] = names[i].strip()
                i += 1

        matching_names = []
        i = 0
        while i < len(names):
            if names[i].lower().startswith(word[0].lower()):
                matching_names.append(names[i])
            i += 1

        if len(matching_names) == 0:
            print("No names in the source file start with the same letter as the word!")
            return "Bob"

        past_names = []
        if os.path.exists(past):
            with open(past, 'r') as past_file:
                past_names_raw = past_file.readlines()
                i = 0
                while i < len(past_names_raw):
                    past_names.append(past_names_raw[i].strip())
                    i += 1

        last_b_name = None
        i = len(past_names) - 1
        while i >= 0:
            if len(past_names[i]) > 0 and past_names[i][0].lower() == word[0].lower():
                j = 0
                while j < len(matching_names):
                    if past_names[i] == matching_names[j]:
                        last_b_name = past_names[i]
                        break
                    j += 1
            if last_b_name is not None:
                break
            i -= 1

        if last_b_name is None:
            new_name = matching_names[0]
        else:
            last_b_index = matching_names.index(last_b_name)
            new_name = matching_names[(last_b_index + 1) % len(matching_names)]

        with open(past, 'a') as past_file:
            past_file.write(new_name + '\n')

        return new_name

    except FileNotFoundError:
        print("Source file is not found!")
        return "Bob"



def main():
    src = "/home/files/animals.txt"
    past = "/home/files/names.txt"
    file_records = "/home/files/history.txt"
    database = '/home/files/list.txt'
    records = '/home/files/history.txt'

    while True:
        word = input("Check name: ").strip().lower()
        if word == "s":
            break

        # Check if name is valid
        if is_valid_name(word) and not is_profanity(word):
            print(f"{word} is a valid name!")
        else:
            new_name = generate_name(word, src, past)
            print(f"Your new name is: {new_name}")


if __name__ == "__main__":
    main()
