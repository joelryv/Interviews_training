"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
"""
class Solution:
    def reverse(self, x: int) -> int:
        n=0
        if x<0:
            n=-int(str(-x)[::-1]) 
        else:
            n= int(str(x)[::-1])
        return n if n.bit_length()<32 else 0