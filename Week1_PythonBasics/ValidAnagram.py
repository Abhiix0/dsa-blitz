class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

#this problem can be solved in O(n) time complexity by using two hash maps to count the occurrences of each character in both strings. We first check if the lengths of the two strings are equal; if not, they cannot be anagrams. Then, we iterate through each character in both strings and update their respective counts in the hash maps. Finally, we compare the counts of each character in both hash maps. If they match for all characters, the strings are anagrams; otherwise, they are not.