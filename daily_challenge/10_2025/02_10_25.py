"""
https://leetcode.com/problems/water-bottles-ii/submissions/1788889507/?envType=daily-question&envId=2025-10-02
"""

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        totalDrunk = 0
        while numBottles > 0:
            totalDrunk += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                numBottles += 1
        return totalDrunk
    

