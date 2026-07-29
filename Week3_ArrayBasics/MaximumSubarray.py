class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
       current = nums[0]
       best = nums[0]
       for num in nums[1:]:
        current = max(num, current + num)
        best = max(current, best)
       return best

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We maintain two variables: current, which keeps track of the maximum subarray sum ending at the current position, and best, which keeps track of the overall maximum subarray sum found so far. We iterate through the list starting from the second element, updating current to be the maximum of the current number or the sum of current and the current number. We then update best to be the maximum of best and current. Finally, we return best as the result.