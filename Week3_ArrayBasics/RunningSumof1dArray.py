class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        r = []
        for i in nums:
            total += i
            r.append(total)
        return r

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We iterate through the input list and maintain a running total of the sum of elements encountered so far. For each element, we add it to the running total and append the current total to a new list. Finally, we return the new list containing the running sums.