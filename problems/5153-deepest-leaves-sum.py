# tree, dfs
# https://leetcode-cn.com/problems/deepest-leaves-sum/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# bfs

from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:  
        if root is None:
            return 0

        queue = deque([(1, root)])
        cur_depth, cur_sum = 1, root.val

        while queue:
            depth, node = queue.popleft()
            # reaches a new depths
            if depth > cur_depth:
                cur_depth, cur_sum = depth, 0
            
            cur_sum += node.val
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
        return cur_sum

