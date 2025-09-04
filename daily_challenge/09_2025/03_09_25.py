"""
https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04
"""
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1=abs(x-z)
        d2=abs(y-z)
        if d1<d2:
            return 1
        if d2<d1:
            return 2 
        else:
            return 0
        
