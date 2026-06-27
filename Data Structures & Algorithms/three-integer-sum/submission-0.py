class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            if i > 0 and nums[i - 1] == v:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = v + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while r > l and nums[r+1] == nums[r]:
                        r -= 1
            
        return res
        