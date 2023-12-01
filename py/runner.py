"""
Driver for running a given Year/Day/Part with the default input.
"""

import sys
import os
from importlib import import_module

HELP_TEXT = "Usage: runner [year_number] [day_number] [part_number]"
INVALID_PART_TEXT = "Invalid year, day, and/or part given: {} {} {}"

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

def exit_invalid_part(year, day, part):
    """
    Exits with INVALID_PART_TEXT formatted for a given day/part, and exit code 2.

    :param year: The given year.
    :type year: int
    :param day: The given day.
    :type day: int
    :param part: The given part.
    :type part: int
    """
    exit_with_msg_and_code(INVALID_PART_TEXT.format(year, day, part), 2)

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
    Parse the year/day/part number from argv.
    Load the module for the given part.
    Run that module's answer func with the default input for that part.
    Print the answer.
    """

    if len(sys.argv) != 4:
        exit_help()

    year_number = try_int(sys.argv[1])
    day_number = try_int(sys.argv[2])
    part_number = try_int(sys.argv[3])

    script_path = os.path.dirname(os.path.abspath(__file__))
    # Use the default input for the given day
    input_path = f"{script_path}/../inputs/{year_number}/{day_number}.txt"

    module_name = f"_{year_number}._{day_number}._{part_number}"
    try:
        module = import_module(module_name)
    except ModuleNotFoundError as e:
        raise e
        exit_invalid_part(year_number, day_number, part_number)

    with open(input_path, encoding='ascii') as file:
        print(module.answer(file))

    sys.exit(0)

if __name__ == "__main__":
    run()
