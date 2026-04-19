class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    order = []

    def recurse(node, order):
        if not (node.left or node.right):
            return order + [node.data]

        order = order + [node.data]

        if node.left is not None:
            order = recurse(node.left, order)

        if node.right is not None:
            order = recurse(node.right, order)

        return order
    if not isinstance(node, Node):
        return []
    return recurse(node, order)


# In-order traversal
def in_order(node):
    order = []

    def recurse(node, order):
        if not (node.left or node.right):
            return order + [node.data]

        if node.left is not None:
            order = recurse(node.left, order)

        order = order + [node.data]

        if node.right is not None:
            order = recurse(node.right, order)

        return order

    if not isinstance(node, Node):
        return []
    return recurse(node, order)

# Post-order traversal
def post_order(node):
    order = []

    def recurse(node, order):
        if not (node.left or node.right):
            return order + [node.data]

        if node.left is not None:
            order = recurse(node.left, order)

        if node.right is not None:
            order = recurse(node.right, order)

        order = order + [node.data]

        return order
    if not isinstance(node, Node):
        return []
    return recurse(node, order)


'''leaf_7 = Node(7)
leaf_6 = Node(6)
leaf_5 = Node(5)
leaf_8 = Node(8)
leaf_9 = Node(9)
root_3 = Node(3, leaf_8, leaf_9)
root_4 = Node(4, leaf_6, leaf_7)
root_2 = Node(2, root_4, leaf_5)
root = Node(1, root_2, root_3)

print(post_order(root))
print(pre_order(root))
print(in_order(root))
print(post_order(Node(10)))
'''
