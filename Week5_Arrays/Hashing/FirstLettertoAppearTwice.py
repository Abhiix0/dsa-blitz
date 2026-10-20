class Solution:
    def repeatedCharacter(self, s: str) -> str:
        r = set()
        for ch in s:
            if ch in r:
                return ch
            else:
                r.add(ch)

#this problem can be solved using a set data structure. The function repeatedCharacter takes a string s as input and returns the first character that appears twice in the string. It iterates through each character in the input string, checking if it is already present in the set r. If it is, the function returns that character as it is the first one to appear twice. If not, the character is added to the set for future reference.