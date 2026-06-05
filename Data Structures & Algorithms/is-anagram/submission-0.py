from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower()
        t=t.lower()
        return Counter(s)==Counter(t)
        