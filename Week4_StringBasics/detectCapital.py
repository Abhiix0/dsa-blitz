class Solution(object):
    def detectCapitalUse(self, word):
        if word == word.upper():
            return True

        if word == word.lower():
            return True

        if 'A' <= word[0] <= 'Z':
            for i in range(1, len(word)):
                if not word[i].islower():
                    return False
            return True

        return False

#This problem can be solved in O(n) time complexity, where n is the length of the input string. We check if the entire word is uppercase or lowercase, which are valid cases. If the first character is uppercase, we then check that all subsequent characters are lowercase. If any character does not meet these conditions, we return False. Otherwise, we return True for valid capital usage.