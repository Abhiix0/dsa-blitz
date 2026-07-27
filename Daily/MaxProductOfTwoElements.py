class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        first = 0
        second = 0

        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        return (first - 1) * (second - 1)

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We iterate through the list once to find the two largest numbers. We maintain two variables, first and second, to keep track of the largest and second largest numbers encountered so far. For each number in the list, we check if it is greater than first; if it is, we update second to be first and first to be the current number. If it is not greater than first but greater than second, we update second to be the current number. Finally, we return the product of (first - 1) and (second - 1) as the result.