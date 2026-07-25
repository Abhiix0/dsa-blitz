class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        a = 0 
        b = 0 
        n = len(nums)
        for num in range(0, n+1):
            a += num
        for num in nums:
            b += num
        c = a - b
        return c

#this problem can be solved in O(n) time complexity by using the formula for the sum of the first n natural numbers. We calculate the expected sum of numbers from 0 to n using the formula n*(n+1)/2, and then we calculate the actual sum of the numbers present in the input list. The missing number can be found by subtracting the actual sum from the expected sum. Finally, we return the missing number.