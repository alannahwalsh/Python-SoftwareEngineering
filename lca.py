# Python Program for Lowest Common Ancestor in a Binary Tree
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
