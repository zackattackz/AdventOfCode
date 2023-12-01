# Python Solutions

This is a python package that contains all the solutions for the parts of AoC I've attempted.

As general rules I try to:
1. Use as much idomatic python as possible.
2. Only use the python standard library.
3. Use generators wherever they might reasonably improve performance / memory consumption
    * (In other words, avoid generators if the gains are negligible)
4. Decouple functionality between Parts as much as possible.

## Package Layout

Each day's solutions are located in their respective sub-package:

* Year 2022 Day 1 is in `_2022/_1`
* Year 2022 Day 2 is in `_2022/_2`
* etc...

### Sub-package layout
Within each solution sub-package, there is a `_1.py` module and a `_2.py` module.

`_1.py` corresponds to the Part 1 solution of that Day and `_2.py` corresponds to the Part 2 solution.

`_1.py` and `_2.py` both define the `answer` function.

`answer` takes in an open file (containing the problem input)
as an argument and returns the answer for that input.

The sub-packages also define their own common utilities used between `_1.py` and `_2.py`,
for example `_1/parse.py` contains a parser for the Day 1 Part 1 and 2 input.

## Runner
This package also contains `runner.py`, which is a driver for running the solutions.

To run the solution for a given Year/Day/Part, run the following from the `py` directory (this package):

```
./runner YEAR DAY PART

# example to run the year 2022 day 2 part 1 solution...
./runner 2022 2 1
```

Where YEAR, DAY, and PART are numbers representing which year, day, and which part you wish to run.

Runner works simply by opening the input file for the given Year/Day, and prints the result of `answer(file)` for the given Year/Day/Part.