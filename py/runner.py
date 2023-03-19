"""
Driver for running a given Day/Part with the default input.
"""

import sys
from importlib import import_module

HELP_TEXT = "Usage: runner [day_number] [part_number]"
INVALID_PART_TEXT = "Invalid day and/or part given: {} {}"

def exit_with_msg_and_code(msg, code):
    """
    Exit the program with code, print msg to stderr.

    :param msg: Error message to print to stderr.
    :type msg: str
    :param code: Exit code to exit with.
    :type code: int
    """
    print(msg, file=sys.stderr)
    sys.exit(code)

def exit_help():
    """
    Exits with HELP_TEXT and exit code 1
    """
    exit_with_msg_and_code(HELP_TEXT, 1)

def exit_invalid_part(day, part):
    """
    Exits with INVALID_PART_TEXT formatted for a given day/part, and exit code 2.

    :param day: The given day.
    :type day: int
    :param part: The given part.
    :type part: int
    """
    exit_with_msg_and_code(INVALID_PART_TEXT.format(day, part), 2)

def try_int(val):
    """
    Tries to convert value to an int, but exits if ValueError is raised.

    :param val: The value to convert.
    :return: int
    """
    try:
        return int(val)
    except ValueError:
        return exit_help()

def run():
    """
    Parse the day/part number from argv.
    Load the module for the given day/part.
    Run that module's answer func with the default input for that day.
    Print the answer.
    """

    if len(sys.argv) != 3:
        exit_help()

    day_number = try_int(sys.argv[1])
    part_number = try_int(sys.argv[2])

    # Use the default input for the given day
    input_path = f"../inputs/{day_number}.txt"

    module_name = f"_{day_number}._{part_number}"
    try:
        module = import_module(module_name)
    except ModuleNotFoundError:
        exit_invalid_part(day_number, part_number)

    with open(input_path, encoding='ascii') as file:
        print(module.answer(file))

    sys.exit(0)

if __name__ == "__main__":
    run()
