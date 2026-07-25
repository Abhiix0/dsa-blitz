class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        for c in ransomNote:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1
        return True

#this problem can be solved in O(n) time complexity by using a hash map to count the occurrences of each character in the magazine string. We first iterate through the magazine string and populate the hash map with the counts of each character. Then, we iterate through the ransomNote string and check if each character is present in the hash map and has a non-zero count. If any character is not present or has a count of zero, we return False. If we successfully check all characters in ransomNote, we return True, indicating that it can be constructed from the magazine.