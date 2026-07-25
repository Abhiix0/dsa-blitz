class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set1 = set(sentence)
        return len(set1) == 26

#this problem can be solved in O(n) time complexity by using a set to store the unique characters in the input string. We iterate through the string and add each character to the set. After processing the entire string, we check if the size of the set is equal to 26, which indicates that all letters of the English alphabet are present in the string. If the size is 26, we return True; otherwise, we return False.