# tree, dfs

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive dfs
class Solution:
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left) + 1
        depth_right = self.maxDepth(root.right) + 1
        return max(depth_left, depth_right)


# iterative dfs
class Solution:
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0

        stack, max_depth = [(1, root)], 1
        while stack:
            depth, node = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((depth+1, node.left))
            if node.right:
                stack.append((depth+1, node.right))
        return max_depth


# iterative bfs
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0

        # using deque in BFS reduces the run time a lot
        queue = deque([(1, root)])
        while queue:
            depth, node = queue.popleft()
            # we don't need to compare the depth when using BFS
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
        return depth


