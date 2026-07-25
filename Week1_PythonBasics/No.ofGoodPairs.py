from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = {}
        good_pairs = 0
        for num in nums:
            if num in counts:
                good_pairs += counts[num]
                counts[num] += 1
            else:
                counts[num] = 1
                
        return good_pairs

#this problem can be solved in O(n) time complexity by using a hash map to count the occurrences of each number in the input list. We iterate through the list and for each number, we check if it has been seen before. If it has, we add the count of that number to the good_pairs variable, as each previous occurrence can form a good pair with the current occurrence. We then increment the count of that number in the hash map. Finally, we return the total count of good pairs.