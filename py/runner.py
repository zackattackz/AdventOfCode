import sys
from importlib import import_module

HELP_TEXT = "Usage: runner [day_number] [part_number]"

def exit_with_msg_and_code(msg, code):
    print(msg, file=sys.stderr)
    exit(code)

def exit_help():
    exit_with_msg_and_code(HELP_TEXT, 1)

def try_int(s):
    try:
        return int(s)
    except ValueError:
        exit_help()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit_help()
    [day_number, part_number] = [try_int(s) for s in sys.argv[1:]]
    input_path = f"inputs/{day_number}.txt"
    module_name = f"_{day_number}._{part_number}"
    module = import_module(module_name)
    with open(input_path) as f:
        print(module.answer(f))
    exit(0)
