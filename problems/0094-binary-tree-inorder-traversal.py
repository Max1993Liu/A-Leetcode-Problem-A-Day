# stack, tree, hash table
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/


# recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return None

        res = []
        def helper(node):
            if node.left:
                helper(node.left)    
            res.append(node.val)
            if node.right:
                helper(node.right)

        helper(root)
        return res
