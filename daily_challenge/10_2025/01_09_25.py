"""
https://leetcode.com/problems/water-bottles/description/?envType=daily-question
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while True:
            exchange = numBottles//numExchange
            if exchange == 0:
                return total
            total += exchange

