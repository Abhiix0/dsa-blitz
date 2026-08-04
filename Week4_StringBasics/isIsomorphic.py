class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}

        for c1, c2 in zip(s, t):

            if c1 in st:
                if st[c1] != c2:
                    return False

            elif c2 in ts:
                return False

            else:
                st[c1] = c2
                ts[c2] = c1

        return True
#this problem can be solved in O(n) time complexity, where n is the length of the input strings. We use two dictionaries to keep track of the character mappings from s to t and from t to s. We iterate through both strings simultaneously, checking if the current characters have been seen before and if their mappings are consistent. If we find any inconsistencies, we return False. If we finish iterating through both strings without finding any issues, we return True, indicating that the strings are isomorphic.