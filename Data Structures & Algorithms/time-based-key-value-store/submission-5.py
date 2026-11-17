class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #strictly increasing timestamps, so timestamps are sorted
        self.map[key] = self.map.get(key,[]) + [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not self.map.get(key):return""
        l, r = 0, len(self.map[key])-1

        while l<=r:
            mid = (l+r)//2
            if self.map[key][mid][1] > timestamp:
                r = mid-1
            else:
                l = mid+1

        if r < 0:return ""
        return self.map[key][r][0]