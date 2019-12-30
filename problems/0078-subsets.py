# bit manipulation, array, backtracking
# https://leetcode-cn.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for elem in nums:
            res += [i + [elem] for i in res]
        return res
