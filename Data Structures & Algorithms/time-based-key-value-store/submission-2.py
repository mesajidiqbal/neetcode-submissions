class TimeMap:

    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append((value, timestamp))      

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.key_store[key]
        if not val:
            return res

        l, r = 0, len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            if val[mid][1] > timestamp:
                r = mid - 1
            else:
                res = val[mid][0]
                l = mid + 1
        return res