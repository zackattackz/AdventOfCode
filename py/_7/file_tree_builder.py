"""
Defines the FileTreeBuilder class
"""
from itertools import chain
from typing import Iterable, List, Optional
from .command import Command, CdCommand, LsCommand
from .file_tree import FileTree

class NoParentDirectoryException(Exception):
    """Raised when attempting to cd into a parent directory when none exists."""

class NotBuiltException(Exception):
    """
    Raised when attempting to access root file tree
    when it hasn't yet been made.
    """

class FileTreeBuilder:
    """
    Class that builds a FileTree by running commands.

    A file tree for the current working directory is kept.
    It is updated when LsCommands are ran.

    A history of parent file trees is kept a well.
    
    When a CdCommand is ran, the current and history are updated as needed.
    """

    parent_dir_alias = ".."
    """Directory name indicating \"Cd to parent directory\"."""

    def __init__(self, commands: Iterable[Command]):
        self.commands = chain(commands)
        """Commands to run to build the FileTree."""

        self.current_file_tree: Optional[FileTree] = None
        """Represents the file tree for the current working directory(CWD)."""


        self.last_file_trees: List[FileTree] = []
        """
        Stack containing the history of visited file trees.
        Forms an absolute path to CWD's parent.
        """

    def _run_cd_command(self, command: CdCommand):
        """
        Mutate self to reflect result of running cd command.
        """
        if command.dst_name == self.parent_dir_alias:
            # Try to set current dir to the last dir we were in.
            try:
                self.current_file_tree = self.last_file_trees.pop()
                return
            except IndexError as exc:
                raise NoParentDirectoryException() from exc

        file_tree = FileTree(command.dst_name, set())

        if self.current_file_tree:
            # Set parent of the new file tree to be current
            self.current_file_tree.children.add(file_tree)
            self.last_file_trees.append(self.current_file_tree)
        # Set current to be the new file tree
        self.current_file_tree = file_tree

    def _run_ls_command(self, command: LsCommand):
        """
        Mutate self to reflect result of running ls command.
        """
        for file in command.output:
            self.current_file_tree.children.add(file)

    def get_root_file_tree(self) -> FileTree:
        """
        Returns the root file tree if it has been built.

        Raises NotBuiltException if it hasn't been built.
        """
        if len(self.last_file_trees) > 0:
            return self.last_file_trees[0]
        raise NotBuiltException()

    def load_commands(self, commands: Iterable[Command]) -> None:
        """Chain new commands to end of current commands."""
        self.commands = chain(self.commands, commands)

    def run_commands(self) -> None:
        """Run all loaded commands"""
        for command in self.commands:
            if isinstance(command, CdCommand):
                self._run_cd_command(command)
            else: # Guaranteed command.input is a LsCommandInput
                self._run_ls_command(command)
