"""
Defines parser for creating a FileTree from given problem input.

The problem input is a series of commands and their corresponding outputs.
"""

import re
from typing import Iterable, List
from .command import Command, CdCommand, LsCommand
from .file_tree import FileTree, File
from .file_tree_builder import FileTreeBuilder

def parse_ls_command_output(command_str_outputs: List[str]) -> List[File]:
    """
    Parse the Files from a ls command_str_group.
    """
    ls_output_file_regex = r"^(\d+) (.+)$"
    output: List[File] = []
    for command_str_output in command_str_outputs:
        ls_output_file_match = re.match(ls_output_file_regex, command_str_output)

        # Just skip over non-file outputs.
        if not ls_output_file_match:
            continue

        # Create a File from the match and append it to output list.
        size = int(ls_output_file_match.group(1))
        name = ls_output_file_match.group(2)
        output.append(File(name, size))
    return output

def parse_command_str_group(command_str_group: List[str]) -> Command:
    """
    Parse command string group into a Command object.
    """
    command_prompt_rgx = r"^\$ (.+)$"

    command_str_prompt = command_str_group[0]
    command_prompt_match = re.match(command_prompt_rgx, command_str_prompt)

    command_argv_str = command_prompt_match.group(1)
    command_argv = command_argv_str.split(" ")
    command_name = command_argv[0]

    match command_name:
        case CdCommand.name:
            dst_name = command_argv[1]
            return CdCommand(dst_name)
        case LsCommand.name:
            # Parse output from command_str_group
            output = parse_ls_command_output(command_str_group[1:])
            return LsCommand(output)

def split_command_strs(file: Iterable[str]) -> Iterable[List[str]]:
    """
    Generator for splitting problem input into groups of command strings

    Command strings are Lists of strs where the first is the command prompt input ($ argv)
    and the remaining are outputs.
    """
    cmd_start = "$"
    cmd_str_group = []
    for line in file:
        if line[0] == cmd_start and cmd_str_group:
            yield cmd_str_group
            cmd_str_group = [line]
        else:
            cmd_str_group.append(line)
    if cmd_str_group:
        yield cmd_str_group

def parse(problem_input: Iterable[str]) -> FileTree:
    """
    Creates a FileTree from given problem input.
    """
    # Prepare the commands from the file
    problem_input = (line.rstrip() for line in problem_input)
    command_str_groups = split_command_strs(problem_input)
    commands = (parse_command_str_group(command_str_group)
                for command_str_group in command_str_groups)

    # Use FileTreeBuilder to run the commands and produce the FileTree
    builder = FileTreeBuilder(commands)
    builder.run_commands()
    return builder.get_root_file_tree()
