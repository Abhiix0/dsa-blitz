from collections import Counter
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        r = Counter(arr)
        l = []
        for ch in arr:
            if r[ch] == 1:
                l.append(ch)
        if len(l) >= k:
            return l[k-1]
        else: 
            return ""

#this problem can be solved using a hash map data structure. The function kthDistinct takes a list of strings and an integer k as input and returns the kth distinct string in the list. It uses a Counter to count the occurrences of each string in the input list. Then, it iterates through the original list, checking if each string has a count of 1 (indicating it is distinct). If it is distinct, it is added to a new list l. Finally, if the length of l is greater than or equal to k, the function returns the kth distinct string (at index k-1); otherwise, it returns an empty string.