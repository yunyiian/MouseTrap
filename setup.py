'''
Write your solution for 6. PIAT: Check Setup here.

Author: Yun Yi Ian Chang 
SID: 530317166
unikey: ycha5975
'''
import os
import shutil
from datetime import datetime
import sys
# you can make more functions or global read-only variables here if you please!

def flags():
    if len(sys.argv) < 3:
        sys.stderr.write("Insufficient arguments.\n")
        return None, None

    master = sys.argv[1]
    if not (master.startswith("/") and master.endswith("/")):
        sys.stderr.write("Invalid master directory.\n")
        return None, None
    elif not os.path.isdir(master):
        sys.stderr.write("Invalid master directory.\n")
        return None, None

    flags = "".join(sys.argv[2:])
    if not flags.startswith("-"):
        sys.stderr.write("Invalid flag. Flag must start with '-'.\n")
        return master, None

    if len(set(flags)) != len(flags):
        sys.stderr.write("Invalid flag. Each character must be unique.\n")
        return master, None

    if flags.find("-iv") != -1 or flags.find("-vi") != -1:
        sys.stderr.write("Invalid flag. Choose verify or install process not both.\n")
        return master, None

    if flags.find("-i") != -1:
        if flags.find("v") != -1:
            sys.stderr.write("Invalid flag. Choose verify or install process not both.\n")
            return master, None
        elif flags.find("l") != -1:
            return master, "-il"
        else:
            return master, "-i"
        
    if flags.find("-v") != -1:
        if flags.find("l") != -1:
            return master, "-vl"
        else:
            return master, "-v"
        
    if flags.find("-l") != -1:
        sys.stderr.write("Invalid flag. Log can only run with install or verify.\n")
        return master, None

    sys.stderr.write("Invalid flag. Character must be a combination of 'v' or 'i' and 'l'.\n")
    return master, None


def time():
    now = datetime.now()
    time = now.strftime('%d %b %Y %H:%M:%S')
    return time


def logging(logs: list, date: str, time: str, base_directory: str = '/home/logs') -> None:
    '''
    Logging function uses a list of strings to write previous output into a
    log file.
    Parameters:
        logs: list, output from verification/installation in the form of list of 
                    strings to write to logging file.
        date: str,  a string representing the date to generate the necessary 
                    directory date must be in the format YYYY-MM-DD as seen in 
                    the specs (ex: 2023-Mar-03 for March 3rd, 2023).
        time: str,  a string representing the time to generate the log file
                    time must be in the format HH_MM_SS as seen in the specs
                    (ex: 14_31_27 for 14:31:27).
        base_directory: str, optional, the base directory where logs will be stored.
    '''
    log_directory = os.path.join(base_directory, date)
    # Create the directory if it doesn't exist
    if not os.path.isdir(log_directory):
        os.makedirs(log_directory)

    # Create a log file with the given time
    log_file_name = os.path.join(log_directory, f"{time}.txt")

    # Write the logs to the log file
    with open(log_file_name, "w") as log_file:
        i = 0
        while i < len(logs):
            log_line = logs[i] + "\n"
            log_file.write(log_line)
            i += 1

def verification(master: str, timestamp: str) -> list:
    '''
    Verification makes sure all files and directories listed in the config file
    are present and match the contents of the master files. 
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the verification process.
    '''
    output = []
    output.append("{} Start verification process.".format(timestamp))

    # 1. Extract absolute paths to directories from given configuration file
    output.append(f"{timestamp} Extracting paths in configuration file.")
    config_file = os.path.join(master, "config.txt")
    with open(config_file, "r") as f:
        config_lines = f.readlines()

    directories_to_check = []
    i = 0
    while i < len(config_lines):
        line = config_lines[i].strip()
        if line.startswith("/") and not line.startswith("./") and line.find(".") == -1:
            directories_to_check.append(line)
        i += 1
    output.append(f"Total directories to check: {len(directories_to_check)}")

    # 2. Check if directories exist
    output.append(f"{timestamp} Checking if directories exists.")
    i = 0
    while i < len(directories_to_check):
        directory = directories_to_check[i]
        if os.path.exists(directory):
            output.append(f"{directory} is found!")
        else:
            output.append(f"{directory} not found.")
            break
        i += 1

    # 3. Extract all absolute paths of all files from given configuration file
    output.append(f"{timestamp} Extracting files in configuration file.")
    file_paths = []
    current_directory = None

    with open(config_file, "r") as config_file:
        lines = config_file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line.startswith("./"):
                current_directory = line
            else:
                dest_file_path = os.path.join(current_directory, line[2:])
                file_paths.append(dest_file_path)
                output.append(f"File to check: {dest_file_path}")
            i += 1

    output.append(f"Total files to check: {len(file_paths)}")

    # 4. Check if files exist
    output.append(f"{timestamp} Checking if files exists.")
    i = 0
    while i < len(file_paths):
        file_path = file_paths[i]
        if os.path.exists(file_path):
            output.append(f"{file_path} found!")
        else:
            output.append(f"{file_path} not found.")
            return output
        i += 1

    # Step 5: Check contents of each file with those in the master folder
    output.append(f"{timestamp} Check contents with master copy.")
    file_paths = sorted(file_paths)  # sorting files in alphabetical order
    error_encountered = False
    file_index = 0
    while file_index < len(file_paths):
        file_path = file_paths[file_index]
        master_file_path = os.path.join(master, os.path.relpath(file_path, master))
        while True:
            index = master_file_path.find("../")
            if index != -1:
                master_file_path = master_file_path[:index] + master_file_path[index+3:]
            else:
                break

        if not os.path.exists(master_file_path):
            output.append(f"Missing master copy: {master_file_path}")
            error_encountered = True
            break  # return immediately if master file does not exist

        file_identical = True
        with open(file_path, "r") as dest_file, open(master_file_path, "r") as master_file:
            dest_lines = dest_file.readlines()
            master_lines = master_file.readlines()

            line_num = 0
            while line_num < len(dest_lines):
                dest_line = dest_lines[line_num].strip()
                master_line = master_lines[line_num].strip()

                if dest_line != master_line:
                    # Append all lines up to the mismatch
                    i = 0
                    while i < line_num:
                        output.append(f"File name: {file_path}, {dest_lines[i].strip()}, {master_lines[i].strip()}")
                        i += 1

                    output.append(f"File name: {file_path}, {dest_line}, {master_line}")
                    output.append("Abnormalities detected...")
                    return output
                line_num += 1

        if file_identical:
            output.append(f"{file_path} is same as {master_file_path}: {file_identical}")
        file_index += 1


    output.append(f"{timestamp}  Verification complete.")
    return output


def installation(master: str, timestamp: str) -> list:
    '''
    Installation copies all required master files into the addresses listed by
    the config file.
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the installation process.
    '''
    output = []
    output.append("{} Start installation process.".format(timestamp))

    # 1. Extract absolute paths to directories from given configuration file
    output.append(f"{timestamp} Extracting paths in configuration file.")
    config_file = os.path.join(master, "config.txt")
    with open(config_file, "r") as f:
        config_lines = f.readlines()
    
    directories_to_create = []
    i = 0
    while i < len(config_lines):
        line = config_lines[i].strip()
        if not line.startswith("./"):
            directories_to_create.append(line)
        i += 1
    output.append(f"Total directories to create: {len(directories_to_create)}")

    # 2. Create new directories
    output.append(f"{timestamp} Create new directories.")
    i = 0
    while i < len(directories_to_create):
        directory = directories_to_create[i]
        if not os.path.exists(directory):
            os.makedirs(directory)
            output.append(f"{directory} is created successfully.")
        else:
            output.append(f"{directory} exists. Skip directory creation.")
        i += 1

    # 3. Extract all absolute paths of all files found in the master directory
    output.append(f"{timestamp} Extracting paths of all files in {master}.")
    def sort_key(item):
        return item[0]

    all_files = []
    root_files_iterator = os.walk(master)

    file_path_list = []

    while True:
        try:
            root, _, files = next(root_files_iterator)
        except StopIteration:
            break

        j = 0
        while j < len(files):
            file = files[j]
            if file != "config.txt":
                file_path = os.path.join(root, file)
                file_path_list.append((file_path, file))
            j += 1

    # Sort file paths in alphabetical order
    file_path_list.sort(key=sort_key)

    i = 0
    while i < len(file_path_list):
        file_path, file = file_path_list[i]
        all_files.append(file_path)
        output.append(f"Found: {file_path}")
        i += 1

    # 4. Create new files
    output.append(f"{timestamp}  Create new files.")
    file_paths = []
    current_directory = None

    with open(config_file, "r") as config_file:
        lines = config_file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("/") and not line.startswith("./") and line.find(".") == -1:
                current_directory = line
            else:
                dest_file_path = os.path.join(current_directory, line[2:])
                file_paths.append(dest_file_path)
                output.append(f"Creating file: {dest_file_path}")
                open(dest_file_path, "w")
            i += 1

    # 5. Copy files from master directory accordingly
    output.append(f"{timestamp} Copying files.")
    error_occurred = False
    dest_file_index = 0

    while dest_file_index < len(file_paths):
        dest_file_path = file_paths[dest_file_index]
        found = False
        file_path_index = 0

        while file_path_index < len(file_path_list):
            file_path, file = file_path_list[file_path_index]

            joined_path = os.path.join(master, os.path.relpath(dest_file_path, master))
            while True:
                index = joined_path.find("../")
                if index != -1:
                    joined_path = joined_path[:index] + joined_path[index+3:]
                else:
                    break

            if file_path == joined_path:
                found = True
                output.append(f"Locating: {os.path.basename(dest_file_path)}")
                output.append(f"Original path: {file_path}")
                output.append(f"Destination path: {dest_file_path}")
                try:
                    shutil.copyfile(file_path, dest_file_path)
                except FileNotFoundError:
                    output.append(f"Original path: {file_path} is not found.")
                    error_occurred = True
                break

            file_path_index += 1

        if not found:
            output.append(f"Locating: {os.path.basename(dest_file_path)}")
            output.append(f"Original path: {joined_path} is not found.")
            error_occurred = True

        dest_file_index += 1

    if error_occurred:
        output.append("Installation error...")
    else:
        output.append(f"{timestamp}  Installation complete.")
    return output


def main(master: str, flags: str, timestamp: str):
    '''
    Ideally, all your print statements would be in this function. However, this is
    not a requirement.
    Parameters:
        master:    str, a string representing the absolute path to the master directory.
        flags:     str, a string representing the specified flags, if no flag is given
                        through the command line, flags will be an empty string.
        timestamp: str, a string representing the time to insert into the output.
                    in the format: DD MMM YYYY HH:MM:DD , ex: 10 Apr 2023 12:44:17
    '''
    dt_object = datetime.strptime(timestamp, '%d %b %Y %H:%M:%S')
    
    # Now we can use strftime to format the datetime object into the desired format
    date = dt_object.strftime('%Y-%b-%d')
    time = dt_object.strftime('%H_%M_%S')


    if flags == "-i":
        output = installation(master, timestamp)
        i = 0
        while i < len(output):
            print(output[i])
            i += 1

    elif flags == "-v":
        output = verification(master, timestamp)
        i = 0
        while i < len(output):
            print(output[i])
            i += 1

    elif flags == "-vl" or flags == "-lv":
        logs = verification(master, timestamp)
        logging(logs, date, time)
        i = 0
        while i < len(logs):
            print(logs[i])
            i += 1

    elif flags == "-il" or flags == "-li":
        logs = installation(master, timestamp)
        logging(logs, date, time)
        i = 0
        while i < len(logs):
            print(logs[i])
            i += 1
    else:
        pass

if __name__ == "__main__":
    # you will need to pass in some arguments here
    # we will leave this empty for you to handle the implementation
    master, flags = flags()
    timestamp = time()
    main(master, flags, timestamp)
    
