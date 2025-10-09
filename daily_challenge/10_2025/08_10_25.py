"""
https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/?envType=daily-question&envId=2025-10-09
"""

from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        done = [0] * (len(skill) + 1)
        for i in range(len(mana)):
            for j in range(len(skill)):
                done[j + 1] = max(done[j + 1], done[j]) + mana[i] * skill[j]
            for k in range(len(skill)-1, 0, -1):
                done[k] = done[k + 1] - mana[i] * skill[k]

        return done[-1]