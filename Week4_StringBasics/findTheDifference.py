class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return ch

            freq[ch] -= 1

            if freq[ch] < 0:
                return ch

#this problem can be solved in O(n) time complexity, where n is the length of the longer string t. We use a dictionary to count the frequency of each character in string s. Then, we iterate through string t and check if each character exists in the frequency dictionary. If a character from t is not found in the dictionary or its frequency becomes negative, we return that character as the extra character in t.