class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

#Notes: this problem can be solved in O(n) time complexity using a hash map to store the indices of the numbers we have seen so far. As we iterate through the list, we calculate the difference between the target and the current number. If this difference is already in our hash map, it means we have found the two numbers that add up to the target, and we return their indices. If not, we add the current number and its index to the hash map and continue iterating.