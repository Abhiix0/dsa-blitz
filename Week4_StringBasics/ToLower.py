class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

#this problem can be solved in O(n) time complexity, where n is the length of the input string. We use the built-in lower() method to convert all uppercase letters in the string to lowercase. The method iterates through each character in the string and converts it if it is an uppercase letter, while leaving other characters unchanged. Finally, we return the modified string.