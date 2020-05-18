# Hash Table, Two Pointers, String, Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # mapping from element value to its index
        if s == '':
            return 0

        mapping = dict()
        left, length = 0, 0


        for right, ch in enumerate(s):
    
            if ch in mapping:
                # found duplicates
                left = max(left, mapping[ch] + 1)
     
            length = max(length, right-left+1)
            mapping[ch] = right

        return max(length, right-left+1)



if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("alouzxilkaxkufsu"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
