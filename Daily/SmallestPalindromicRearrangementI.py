from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        left = []
        mid = ""

        for ch in sorted(count):
            freq = count[ch]

            left.append(ch * (freq // 2))

            if freq % 2:
                mid = ch

        left = "".join(left)

        return left + mid + left[::-1]

#This problem can be solved in O(n log n) time complexity, where n is the length of the input string. We use a Counter to count the occurrences of each character in the input string. We then iterate through the sorted characters and build the left half of the palindrome by appending half of the frequency of each character to a list. If a character has an odd frequency, we store it as the middle character. Finally, we construct the palindrome by concatenating the left half, the middle character (if any), and the reverse of the left half, and return it as the result.
