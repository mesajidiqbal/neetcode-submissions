class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums))]
        for n, c in count.items():
            freq[c-1].append(n)

        result = []
        for i in range(len(nums)-1, -1, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result