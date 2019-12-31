# geometry, array
# https://leetcode-cn.com/problems/minimum-time-visiting-all-points/
from typings import List


def minimum_time_between_two_point(a: List[int], b: List[int]):
    diff_x = abs(a[0] - b[0])
    diff_y = abs(a[1] - b[1])
    return min(diff_x, diff_y) + abs(diff_y - diff_x)


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            time += minimum_time_between_two_point(points[i], points[i+1])
        return time
