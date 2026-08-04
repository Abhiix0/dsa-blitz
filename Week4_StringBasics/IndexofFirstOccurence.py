class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for start in range(len(haystack) - len(needle) + 1):
            if haystack[start:start + len(needle)] == needle:
                return start
        return -1

#this problem can be solved in O(n*m) time complexity, where n is the length of the haystack and m is the length of the needle. We iterate through the haystack, checking each substring of length equal to the needle. If a match is found, we return the starting index; otherwise, we return -1 if no match is found after checking all possible substrings.