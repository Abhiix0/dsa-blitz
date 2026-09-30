class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left+1, right+1]
            if summ < target:
                left+=1
            else:
                right-=1

#this problem can be solved using two pointer approach as the array is sorted. We can start with two pointers, one at the beginning and one at the end of the array. We can calculate the sum of the two numbers at these pointers and compare it with the target. If the sum is equal to the target, we return the indices of these two numbers. If the sum is less than the target, we move the left pointer to the right to increase the sum. If the sum is greater than the target, we move the right pointer to the left to decrease the sum. We continue this process until we find the two numbers that add up to the target or until the pointers cross each other.