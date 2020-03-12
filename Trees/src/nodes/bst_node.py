import copy
from typing import Generic, Iterable, TypeVar, Optional
from Trees.src.errors import MissingValueError, EmptyTreeError


T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """

        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def insert(self, input):
        if input == self.value or input > self.value:
            if self.right:
                return self.right.insert(input)
            else:
                self.right = BSTNode(input, parent=self)
                return None
        elif input < self.value:
            if self.left:
                return self.left.insert(input)
            else:
                self.left = BSTNode(input, parent=self)
                return None

    def get_max(self):
        if not self.right:
            return self
        else:
            return self.right.get_max()

    def get_min(self):
        if not self.left:
            return self
        else:
            return self.left.get_min()


    def get(self, input):
        if input == self.value:
            return self
        elif input < self.value:
            if self.left:
                return self.left.get(input)
            else:
                raise MissingValueError
        elif input > self.value:
            if self.right:
                return self.right.get(input)
            else:
                raise MissingValueError

    def delete_node(self, node):
        if self.left == node:
            self.left = None
            return None
        elif self.right == node:
            self.right = None
            return None
        else:
            if node.value < self.value:
                return self.left.delete_node(node)
            elif node.value > self.value:
                return self.right.delete_node(node)


    def remove(self, value):
        node = self.get(value)
        if not node.left and not node.right:
            self.delete_node(node)
        else:
            if self.value == value:
                if self.left and self.right:
                    rep = self.left.get_max()
                    self.delete_node(rep)
                    self.value = rep.value
                    return None
                elif not self.left and self.right:
                    self.value = self.right.value
                    if self.right.left:
                        self.left = self.right.left
                    else:
                        self.left = None
                    if self.right.right:
                        self.right = self.right.right
                    else:
                        self.right = None
                    return None
                elif self.left and not self.right:
                    self.value = self.left.value
                    if self.left.left:
                        self.left = self.left.left
                    else:
                        self.left = None
                    if self.left.right:
                        self.right = self.left.right
                    else:
                        self.right = None
                    return None

            elif value < self.value:
                return self.left.remove(value)
            elif value > self.value:
                return self.right.remove(value)



    def __deepcopy__(self, memodict) -> "BSTNode[T]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        copy_node = BSTNode(copy.deepcopy(self.value, memodict))
        copy_node.left = copy.deepcopy(self.left, memodict)
        copy_node.right = copy.deepcopy(self.right, memodict)
        return copy_node
