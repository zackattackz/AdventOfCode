"""
Defines the SumTree class.
"""

from typing import Self, Set
from .file_tree import FileTree

class SumTreeLockedException(Exception):
    """
    Raised when trying to add children to a locked SumTree.

    A SumTree becomes locked when it is added as a child to another SumTree.

    If you receive this exception you are not using the SumTree in it's intended fashion.
    """

class SumTree:
    """
    A Tree that holds a number value which self-updates on child insertions.

    Useful for pre-computing the nested-sum for all given nodes in a tree structure.
    (O(n) for a tree of n nodes).

    Where self.nested-sum = self.val + nested-sum(child for child in self.children).

    In order for a SumTree to properly compute, it is required
    that children are added "bottom-up".

    i.e: For any given node in a SumTree, before it is added as a child it's parent,
    it's own children must all be added to it.
    """

    def __init__(self, name: str, val: int) -> None:
        """
        :param val: Initial node value.
        """
        self.name = name
        """Name of the node."""

        self.val = val
        """Value of the node plus all it's children's values."""

        self.children: Set[Self] = set()
        """Children nodes."""

        self.locked: bool = False
        """
        Flag indicating whether this node has been added to another as a child.

        If True, no more children can be added to this node.
        """

    @classmethod
    def from_file_tree(cls, file_tree: FileTree) -> Self:
        """
        Create a SumTree from a given FileTree.

        :param file_tree: The FileTree to construct from.
        :return: A SumTree representation of file_tree.
        """
        def build(sum_tree: cls, children: FileTree.Children) -> None:
            """
            Recursive step for building a given sum_tree from given FileTree's children.

            :param sum_tree: The SumTree to build off of.
            :param children: The FileTree children we want to add to sum_tree
            """
            for child in children:
                if isinstance(child, FileTree):
                    child_sum_tree = cls(child.name, 0)
                    build(child_sum_tree, child.children)
                    sum_tree.add_child(child_sum_tree)
                else: # Guaranteed child is a File
                    child_sum_tree = cls(child.name, child.size)
                    sum_tree.add_child(child_sum_tree)

        # Start building from the root of file_tree
        res = cls(file_tree.name, 0)
        build(res, file_tree.children)
        return res

    def add_child(self, child: Self) -> None:
        """
        Add a child to this tree's children and update this tree's value.

        Also locks the child.

        :param child: The child SumTree to add to self.children.
        """
        if self.locked:
            raise SumTreeLockedException()
        child.locked = True
        self.val += child.val
        self.children.add(child)

    def __iter__(self):
        return self.iterator()

    def __repr__(self) -> str:
        return f"SumTree(name={self.name}, val={self.val}, children={self.children})"

    def iterator(self):
        """
        A generator for all the nodes in the tree.
        """
        yield self
        for child in self.children:
            yield from child
