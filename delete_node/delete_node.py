class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def recurse(root, key):
            if root is None:
                return None

            if root.val == key:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                replace_node = root.right
                while replace_node.left:
                    replace_node = replace_node.left

                replace_node.left = root.left

                return root.right

            if key > root.val:
                root.right = recurse(root.right, key)
            else:
                root.left = recurse(root.left, key)

            return root

        recurse(root, key)
        return root

