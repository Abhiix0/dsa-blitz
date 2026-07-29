class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)

#This problem can be solved in O(n) time complexity, where n is the length of the input string. We split the string into words using the split() method, which handles multiple spaces and trims leading/trailing spaces. We then iterate through each word and reverse it using slicing. Finally, we join the reversed words back together with a space separator and return the resulting string.
#return " ".join(word[::-1] for word in s.split())