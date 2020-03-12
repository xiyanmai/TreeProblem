import copy
from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = root

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        def get_height(node):
            if node.left and node.right:
                return 1 + max(get_height(node.left), get_height(node.right))
            elif node.left:
                return 1 + get_height(node.left)
            elif node.right:
                return 1 + get_height(node.right)
            else:
                return 0

        if self.root:
            return get_height(self.root)
        else:
            return -1



    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        def get_length(node):
            if not node:
                return 0
            else:
                if node.right and node.left:
                    return 1 + get_length(node.left) + get_length(node.right)
                elif node.right:
                    return 1 + get_length(node.right)
                elif node.left:
                    return 1 + get_length(node.left)
                else:
                    return 1

        return get_length(self.root)

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        Duplicate values should be placed on the right
        :param value:
        :return:
        """
        if self.root:
            return self.root.insert(value)
        else:
            self.root = BSTNode(value)
            return None

    def remove_value(self, value: K) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        if self.root:
            return self.root.remove(value)
        else:
            raise MissingValueError

    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        if self.root:
            return self.root.get(int(value))
        else:
            raise MissingValueError

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        if self.root:
            return self.root.get_max()
        else:
            raise EmptyTreeError

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        if self.root:
            return self.root.get_min()
        else:
            raise EmptyTreeError



    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __deepcopy__(self, memodict) -> "BST[T,K]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        new_root = copy.deepcopy(self.root, memodict)
        new_key = copy.deepcopy(self.key, memodict)
        return BST(new_root, new_key)


tree = BST()
tree.add_value(100)
tree.add_value(80)
tree.add_value(200)
tree.add_value(300)
tree.add_value(150)

tree.remove_value(200)


