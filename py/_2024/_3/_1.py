import re

from .common import sum_muls

MUL_RGX = re.compile(r"mul\(([0-9]+),([0-9]+)\)")

def matches_to_muls(matches):
    for match in matches:
        yield map(int, match.groups())

def answer(file):
    matches = re.finditer(MUL_RGX, file.read())
    muls = matches_to_muls(matches)
    return sum_muls(muls)

