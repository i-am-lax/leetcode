"""
Two Sum
Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep record of values from nums and corresponding indices
        record = {}
        for idx in range(len(nums)):
            # target number required from nums
            required = target - nums[idx]
            required_idx = record.get(required)
            # if we've already seen the target number we return indices
            if required_idx is not None:
                return [idx, required_idx]
            # else we add a new entry to record
            else:
                record[nums[idx]] = idx


s = Solution()
assert set(s.twoSum(nums=[2, 7, 11, 15], target=9)) == {0, 1}
assert set(s.twoSum(nums=[3, 2, 4], target=6)) == {1, 2}
