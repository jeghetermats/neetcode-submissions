class Solution:

    def encode(self, strs: List[str]) -> str:
        # need to separate [] and [""]
        if strs == []:
            return "æ"
        strs = [i if i!="" else "ø" for i in strs]
        return "æ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s =="æ":
            return []
        s = s.replace("ø","")
        return s.split("æ")