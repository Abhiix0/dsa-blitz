from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        r = Counter(arr)
        s = set()
        for n in r:
            if n == r[n]:
                s.add(n)
        if len(s) == 0:
            return -1
        return(max(s))