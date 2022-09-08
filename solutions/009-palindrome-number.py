"""
Palindrome Number (https://leetcode.com/problems/palindrome-number/)
Difficulty: Easy
"""


class Solution:
    def isPalindromeString(self, x: int) -> bool:
        """Method using string conversion."""
        return str(x) == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        """Method without string conversion."""
        if x < 0:
            return False

        # copy input and set variable for storing reversed result
        number, reverse = x, 0
        while number != 0:
            # isolate last digit
            remainder = number % 10
            # shift to next column and add last digit
            reverse = reverse * 10 + remainder
            # get remaining digits
            number = number // 10

        return reverse == x


s = Solution()
assert s.isPalindrome(121)
assert not s.isPalindrome(1235)
assert s.isPalindromeString(56965)
assert not s.isPalindromeString(-121)
