class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We create an output list initialized with 1s. We first calculate the prefix product for each element by iterating through the input list from left to right, storing the product of all elements before the current index in the output list. Then, we calculate the suffix product by iterating from right to left, multiplying the current value in the output list by the product of all elements after the current index. Finally, we return the output list containing the product of all elements except self for each index.