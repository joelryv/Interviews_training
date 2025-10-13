"""
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13
"""

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            current = sorted(result[-1])
            if sorted(words[i]) != current:
                result.append(words[i])
        return result
    
