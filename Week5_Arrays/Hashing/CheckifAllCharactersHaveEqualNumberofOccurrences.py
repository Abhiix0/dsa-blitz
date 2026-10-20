class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        h = {}
        for ch in s:
            h[ch] = h.get(ch, 0) + 1
        counts = h.values()
        if len(set(counts)) == 1:
            return True
        else:
            return False

#this problem can be solved using a hash map data structure. The function areOccurrencesEqual takes a string s as input and returns a boolean indicating whether all characters in the string have the same number of occurrences. It uses a dictionary h to count the occurrences of each character in the string. After counting, it checks if all counts are equal by converting the values of the dictionary to a set and checking its length. If the length is 1, it means all characters have equal occurrences, and the function returns True; otherwise, it returns False.