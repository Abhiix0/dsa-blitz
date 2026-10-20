class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        common = set(nums[0])
        for num in nums[1:]:
            current = set(num)
            common = common & current
        return sorted(common)

#this problem can be solved using a set data structure. The function intersection takes a list of lists of integers as input and returns a sorted list of integers that are common to all the input lists. It initializes a set common with the elements of the first list. Then, it iterates through the remaining lists, creating a current set for each list and updating the common set by taking the intersection with the current set. Finally, it returns the sorted list of common elements.