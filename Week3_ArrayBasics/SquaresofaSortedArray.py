class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        r = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        w = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                r[w] = nums[left]**2
                left+=1
            else:
                r[w] = nums[right]**2
                right-=1
            w-=1
        return r

#this problem can be solved using two pointer approach as the array is sorted. We can start with two pointers, one at the beginning and one at the end of the array. We can compare the absolute values of the numbers at these pointers and square the larger one, placing it at the end of the result array. We then move the pointer of the larger absolute value towards the center of the array. We continue this process until we have filled the result array with the squares of the numbers in sorted order.