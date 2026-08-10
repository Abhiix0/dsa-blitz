class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1

#this problem can be solved in O(n) time complexity, where n is the length of the input list. We first calculate the total sum of the list, then iterate through each index while maintaining a running sum of the left side. For each index, we calculate the right side by subtracting the left sum and the current element from the total. If the left and right sums are equal, we return the current index. If no such index is found, we return -1.