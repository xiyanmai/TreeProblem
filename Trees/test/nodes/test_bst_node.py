import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode



class TestBSTNode(unittest.TestCase):
    def test_delete_1(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        tree.remove_value(100)

        root = BSTNode(90)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

    def test_delete_2(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        tree.remove_value(80)

        root = BSTNode(100)
        root.left = BSTNode(70)
        root.right = BSTNode(200)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

    def test_delete_3(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        tree.remove_value(200)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

    def test_delete_4(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(300)
        tree.add_value(150)

        tree.remove_value(200)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(150)
        root.right.right = BSTNode(300)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

if __name__ == '__main__':
    unittest.main()
