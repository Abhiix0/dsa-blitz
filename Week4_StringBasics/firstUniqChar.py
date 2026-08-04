from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
                
        for index, char in enumerate(s):
            if counts[char] == 1:
                return index
                
        return -1

#this program finds the index of the first non-repeating character in a given string. It uses the Counter class from the collections module to count the occurrences of each character in the string. Then, it iterates through the string, checking the count of each character. If a character has a count of 1, it returns its index. If no unique character is found, it returns -1.