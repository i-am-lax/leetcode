"""
Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/)
Difficulty: Easy
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort input list to identify shortest word as len(prefix) cannot be > len(shortest word)
        sorted_strs = sorted(strs, key=lambda x: len(x))
        shortest_word = sorted_strs[0]

        # start from shortest word and reduce until prefix is identified else return empty string
        for idx in range(len(shortest_word), 0, -1):
            prefix = shortest_word[:idx]
            if all(word.startswith(prefix) for word in sorted_strs):
                return prefix
            continue
        return ""


s = Solution()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert s.longestCommonPrefix(["mellow", "mighty", "mouse"]) == "m"
