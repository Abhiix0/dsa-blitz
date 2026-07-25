class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        r = 0
        for num in nums:
            r ^= num
        return r
#this problem can be solved in O(n) time complexity by using the XOR operation. The idea is that when we XOR two identical numbers, the result is 0, and when we XOR a number with 0, the result is the number itself. Therefore, if we XOR all the numbers in the list, the pairs of identical numbers will cancel each other out, leaving us with the single number that appears only once.