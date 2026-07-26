class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        max1 = max2 = max3 = float("-inf")
        min1 = min2 = float("inf")

        for num in nums:
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num <= min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We iterate through the list once to find the three largest numbers and the two smallest numbers. The maximum product of three numbers can either be the product of the three largest numbers or the product of the two smallest numbers (which could be negative) and the largest number. We return the maximum of these two products.