class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        for i in range(len(word)):
            ans += (i // 8) + 1

        return ans

#This problem can be solved in O(n) time complexity, where n is the length of the input string. We iterate through each character in the word and calculate the number of pushes required based on its position. Each group of 8 characters requires an additional push, so we use integer division to determine how many complete groups of 8 have been processed and add 1 for the current character. Finally, we return the total number of pushes needed to type the entire word.