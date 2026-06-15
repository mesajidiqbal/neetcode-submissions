class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            reqd = target - num
            if reqd in seen:
                return [seen[reqd], i]
            seen[num] = i
