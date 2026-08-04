class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0

        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))

        return max_words

#this problem can be solved in O(n) time complexity, where n is the total number of characters in all sentences. We iterate through each sentence, split it into words, and count the number of words. We keep track of the maximum word count found so far and return it at the end.