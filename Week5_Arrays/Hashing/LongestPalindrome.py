from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        r = Counter(s)
        counts = r.values()
        even = 0
        for num in counts:
            a = (num//2)*2
            even+=a
        if even < len(s):
            return even + 1 
        else:
            return even

        
#this problem can be solved using a hash map data structure. The function longestPalindrome takes a string s as input and returns the length of the longest palindrome that can be built with the characters in the string. It uses a Counter to count the occurrences of each character in the input string. Then, it iterates through the counts, calculating the number of characters that can be used to form pairs (by integer division by 2 and multiplying by 2). Finally, if the total number of characters used for pairs is less than the length of the input string, it means there is at least one character that can be placed in the center of the palindrome, so it adds 1 to the total length; otherwise, it returns the total length of characters used for pairs.