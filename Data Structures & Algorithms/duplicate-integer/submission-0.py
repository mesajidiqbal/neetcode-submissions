class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for el in nums:
            if el in s:
                return True
            s.add(el)
        return False
        