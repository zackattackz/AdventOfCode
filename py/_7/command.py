"""Defines Commands used in the Day 7 problem"""

from dataclasses import dataclass
from typing import List
from .file_tree import File

@dataclass
class CdCommand:
    """Represents input/output for a cd command."""

    name = "cd"

    dst_name: str
    """The destination directory to cd into."""

@dataclass
class LsCommand:
    """Represents input/output for a ls command."""

    name = "ls"

    output: List[File]
    """All the files listed in the directory."""

Command = CdCommand | LsCommand
