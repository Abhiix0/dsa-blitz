class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))
        r = ""

        for i in range(m):
            r += word1[i]
            r += word2[i]

        r += word1[m:]
        r += word2[m:]
        return r

#This problem can be solved in O(n) time complexity, where n is the length of the longer input string. We iterate through both strings up to the length of the shorter string, appending characters from each string alternately to the result string. After that, we append any remaining characters from the longer string to the result. Finally, we return the merged result string.