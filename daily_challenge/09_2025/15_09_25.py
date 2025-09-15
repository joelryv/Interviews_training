"""
https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brkn = {}
        for c in brokenLetters:
            brkn[c] = 1
        words = text.split()
        valid = len(words)
        for word in words:
            for l in word:
                if l in brkn.keys():
                    valid -= 1
                    break
        return valid
    
