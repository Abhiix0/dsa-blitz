class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        n = set(nums)
        m = -1
        for num in n:
            if num > m and -num in n:
                m = num
        return m

#this problem can be solved using a set data structure. The function findMaxK takes a list of integers as input and returns the largest positive integer k such that both k and -k exist in the list. It first converts the input list into a set n to eliminate duplicates and allow for O(1) lookups. Then, it initializes a variable m to -1 to keep track of the maximum positive integer found. The function iterates through each number in the set, checking if it is greater than m and if its negative counterpart exists in the set. If both conditions are met, m is updated to the current number. Finally, the function returns m, which will be -1 if no such integer was found.