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

#this problem can be solved using a hash map data structure. The function findLucky takes a list of integers as input and returns the largest lucky integer in the list. A lucky integer is defined as an integer that appears in the list exactly as many times as its value. The function uses a Counter to count the occurrences of each integer in the input list. Then, it iterates through the keys of the Counter, checking if the integer is equal to its count. If it is, the integer is added to a set s. Finally, if the set s is empty, it returns -1; otherwise, it returns the maximum value from the set s.