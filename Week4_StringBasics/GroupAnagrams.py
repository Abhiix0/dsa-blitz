class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

#this problem can be solved in O(n * k log k) time complexity, where n is the number of strings in the input list and k is the maximum length of a string. We use a dictionary to group anagrams together by sorting each word and using the sorted tuple as a key. If the key does not exist in the dictionary, we create a new list for that key. Finally, we return the values of the dictionary as a list of lists, where each inner list contains anagrams.