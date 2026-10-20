from collections import Counter
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])
        r = []
        for s in words[1:]:
            current = Counter(s)
            common = common & current
        for char, count in common.items():
            r.extend(char*count)
        return r

#this problem can be solved using a hash map data structure. The function commonChars takes a list of strings as input and returns a list of characters that are common to all strings in the list. It uses a Counter to count the occurrences of each character in the first string and initializes it as the common counter. Then, it iterates through the remaining strings, creating a current counter for each string and updating the common counter by taking the intersection with the current counter. Finally, it constructs the result list by extending it with each character repeated by its count in the common counter and returns the result list.