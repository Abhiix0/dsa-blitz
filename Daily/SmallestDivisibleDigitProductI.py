class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n

        while True:
            product = 1

            for digit in str(current):
                product *= int(digit)

            if product % t == 0:
                return current

            current += 1

# This problem can be solved in O(k * d) time complexity, where k is the number of integers we check and d is the number of digits in each integer. We start from the given integer n and incrementally check each subsequent integer to see if the product of its digits is divisible by t. We calculate the product of digits by converting the integer to a string and multiplying each digit together. Once we find an integer that meets the condition, we return it.