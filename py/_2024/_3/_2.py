import re

from .common import sum_muls

MUL_RGX = re.compile(r"(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)")

def matches_to_muls(matches):
    matches = (m.groups() for m in matches)
    do_flag = True
    for do_g, dont_g, x_g, y_g in matches:
        if do_g:
            do_flag = True
        elif dont_g:
            do_flag = False
        elif do_flag:
            yield int(x_g), int(y_g)

def answer(file):
    matches = re.finditer(MUL_RGX, file.read())
    muls = matches_to_muls(matches)
    return sum_muls(muls)

