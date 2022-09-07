"""
Roman to Integer (https://leetcode.com/problems/roman-to-integer/)
Difficulty: Easy
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # mapping of roman numerals to integer values
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # exception cases whereby for example IV denotes (-1 + 5 = 4) instead of (1 + 5 = 6)
        exceptions = {"IV", "IX", "XL", "XC", "CD", "CM"}
        number = 0
        for idx, val in enumerate(s):
            n = mapping[val]
            # add mapped values together except for special cases where we subtract
            if (idx < len(s) - 1) and (val + s[idx + 1] in exceptions):
                n *= -1
            number += n
        return number


s = Solution()
assert s.romanToInt("III") == 3
assert s.romanToInt("IV") == 4
assert s.romanToInt("LVIII") == 58
assert s.romanToInt("MCMXCIV") == 1994
