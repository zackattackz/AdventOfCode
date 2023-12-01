"""
Defines FileTree and File dataclasses
"""

from dataclasses import dataclass
from typing import Self, Set


@dataclass
class File:
    """
    Represents a file object with a name and size.
    """

    name: str
    """Name of file."""

    size: int
    """Size of file."""

    def __hash__(self) -> int:
        return hash(self.name)

@dataclass
class FileTree:
    """
    Represents a node (directory) in a File Tree. Children are either nodes or Files.
    """

    Children = Set[Self | File]

    name: str
    """Name of node."""

    children: Children
    """Set of child nodes or Files. Files are essentially leafs with extra data."""

    def __hash__(self) -> int:
        return hash(self.name)
