class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cw = {}
        wc = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c in cw:
                if cw[c] != w:
                    return False
            elif w in wc:
                return False
            else:
                cw[c] = w
                wc[w] = c

        return True

#This problem can be solved in O(n) time complexity, where n is the length of the input string. We use two dictionaries to maintain a mapping between characters in the pattern and words in the string. We iterate through both the pattern and the words simultaneously, checking for consistency in the mappings. If any inconsistency is found, we return False. If we successfully map all characters to words without conflict, we return True.