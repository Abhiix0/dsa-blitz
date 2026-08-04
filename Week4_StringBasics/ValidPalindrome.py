class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        return clean == clean[::-1]

#this problem can be solved in O(n) time complexity, where n is the length of the input string. We iterate through the string and build a new string containing only alphanumeric characters in lowercase. Then, we check if this cleaned string is equal to its reverse. If they are equal, the original string is a palindrome; otherwise, it is not.