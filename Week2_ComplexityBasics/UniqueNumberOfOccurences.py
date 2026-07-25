from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        c = Counter(arr)
        return len(c.values()) == len(set(c.values()))

#this problem can be solved in O(n) time complexity by using a hash map to count the occurrences of each number in the input list. We iterate through the list and for each number, we increment its count in the hash map. After counting the occurrences, we check if the values (occurrences) in the hash map are unique by comparing the length of the values with the length of the set of values. If they are equal, it means all occurrences are unique, and we return True; otherwise, we return False.