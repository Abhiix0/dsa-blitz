class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        r = sorted(set(nums))
        if len(r) >= 3:
            return r[-3]
        elif len(r) < 3:
            return r[-1]
        
# This problem can be solved in O(n log n) time complexity, where n is the length of the input array. We first convert the input list to a set to remove duplicates and then sort the unique elements. If there are at least three unique elements, we return the third maximum element; otherwise, we return the maximum element.

