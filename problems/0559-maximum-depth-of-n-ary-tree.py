# tree, bfs, dfs
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# bfs
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
    	if root is None:
    		return 0

    	queue = deque([(1, root)])
    	while queue:
    		depth, node = queue.popleft()
    		if node.children:
    			queue.extend([(depth+1, n) for n in node.children])
    	return depth

