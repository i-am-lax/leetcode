"""
Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
Difficulty: Easy
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # list to store brackets and check matches
        stack = []
        # mapping of open/close brackets
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for letter in s:
            # if open bracket then add to stack
            if letter in mapping:
                stack.append(letter)
            # false if close before open bracket or if close does not match open bracket
            elif len(stack) == 0 or letter != mapping[stack.pop()]:
                return False
        # if stack empty then true otherwise false because single brackets remain
        return len(stack) == 0


s = Solution()
assert s.isValid("()")
assert s.isValid("()[]{}")
assert not s.isValid("(]")
assert s.isValid("([])")
assert not s.isValid("([)]")
