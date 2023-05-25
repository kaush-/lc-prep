# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def internal_serialize(root, string):
            if not root:
                return string + "None,"

            string += str(root.val) + ","
            string = internal_serialize(root.left, string)
            string = internal_serialize(root.right, string)

            return string

        return internal_serialize(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def internal_deserialize(lst):
            if lst[0] == "None":
                lst.pop(0)
                return

            node = TreeNode(lst[0])
            lst.pop(0)

            node.left = internal_deserialize(lst)
            node.right = internal_deserialize(lst)

            return node

        data = data.split(',')
        root = internal_deserialize(data)
        return root
        # Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
