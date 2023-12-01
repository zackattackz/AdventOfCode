# Advent of Code

Here are my solutions to [Advent of Code](https://adventofcode.com/) (AoC) problems 

The root directory contains directories of solutions for given languages (e.g `py/`), and also a `inputs/` directory for each part's input.

In each language's directory, there are CLI programs for each language to be used to run any of my solutions for that given language. e.g. `py/runner` can be used as a driver for running the Python solution for any given Year/Day/Part of the calendar.

See README.md in the language-specific directory for instructions on how to operate it's runner.


## Requirements

I've provided a nix flake (`flake.nix`) with devShell outputs that provide any necessary requirements.

To use it, you need to first install the [Nix Package Manager](https://nixos.org/download) (Or just use NixOS 😉)

Then, you can either run `nix develop` within the repository or you can install [direnv](https://direnv.net/) to automatically do that for you.

Alternatively, if you don't want to install Nix, here is a list of any requirements for you to install at your discretion:

* [Python 3.11](https://www.python.org/downloads/release/python-3110/)