class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        r = []
        for i in candies:
            r.append(i+extraCandies >= m)
        return r
#This problem can be solved in O(n) time complexity, where n is the length of the input list. We first find the maximum number of candies any kid has. Then, we iterate through the list of candies and for each kid, we check if adding the extraCandies to their current number of candies would make it greater than or equal to the maximum number of candies. We store the result (True or False) in a new list and return that list at the end.