# tree, dfs
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        stack, cur = [root], root
        while stack:
            print(stack)
            node = stack.pop()

            # push the right node before left node, so the left node get visited first
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            cur.left, cur.right = None, node
            cur = node
