from collections import Counter
class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        h = Counter(nums)
        pairs = 0
        leftovers = 0
        counts = h.values()
        for num in counts:
            r = num//2
            m = num%2
            pairs += r
            leftovers += m   
        return [pairs, leftovers]

#this problem can be solved using a hash map data structure. The function numberOfPairs takes a list of integers as input and returns a list containing the number of pairs and the number of leftover elements. It uses a Counter to count the occurrences of each integer in the input list. Then, it iterates through the counts, calculating the number of pairs (by integer division by 2) and the number of leftovers (by taking the modulus by 2). Finally, it returns a list containing the total number of pairs and leftovers.