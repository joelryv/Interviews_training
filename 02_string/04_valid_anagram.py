"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, -1) - 1
        for key, value in d.items():
            if value != 0:
                return False
        return True