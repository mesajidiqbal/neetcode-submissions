class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        map = {}

        for ch in s:
            if ch in map:
                map[ch] += 1
            else:
                map[ch] = 1
        
        for ch in t:
            if ch in map:
                map[ch] -= 1
            else:
                map[ch] = 1

        for k, v in map.items():
            if v != 0:
                return False

        return True
