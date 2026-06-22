class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            chars = s[j+1: j+l+1]
            res.append(chars)
            j = j+l+1
            i = j

        return res
