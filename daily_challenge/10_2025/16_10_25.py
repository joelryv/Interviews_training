"""
https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/description/?envType=daily-question&envId=2025-10-17
"""

from typing import List

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        letters_mask = [1 << (ord(letter) - ord("a")) for letter in s]

        def make_prefix(letters_mask: List[int]):
            prefix = [0]
            prefix_mask = [0]
            unique_letters_mask = 0
            partitions = 0
            for letter_mask in letters_mask:
                unique_letters_mask |= letter_mask
                if unique_letters_mask.bit_count() > k:
                    partitions += 1
                    unique_letters_mask = letter_mask
                prefix.append(partitions)
                prefix_mask.append(unique_letters_mask)
            return prefix, prefix_mask

        prefix, prefix_mask = make_prefix(letters_mask)
        suffix, suffix_mask = make_prefix(letters_mask[::-1])

        max_partitions_after_operations = 0
        for index in range(n):
            partitions = prefix[index] + suffix[-(index + 2)]
            # Represents the number of unique letters in the merged left and right
            # substrings if no partition split occurs at index.
            unique_letters_mask = prefix_mask[index] | suffix_mask[-(index + 2)]
            if min(unique_letters_mask.bit_count() + 1, 26) <= k:
                # A new unique letter can be added at this index without exceeding
                # k so we can only make one more partition by combing the left
                # and right substrings at this index.
                partitions += 1
            elif (
                prefix_mask[index].bit_count()
                == suffix_mask[-(index + 2)].bit_count()
                == k
                and unique_letters_mask.bit_count() < 26
            ):
                # Both the left and right substrings are "full" of k unique letters
                # and there is at least one unique letter that is not in either substring
                # so we can create three partitions by flipping the current index.
                partitions += 3
            else:
                # Otherwise we can flip this index to create two partitions between the
                # left and right substrings.
                partitions += 2
            max_partitions_after_operations = max(
                max_partitions_after_operations, partitions
            )
        return max_partitions_after_operations

