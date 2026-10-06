class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        def merge(left: list[int], right: list[int]) -> list[int]:
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return merge(left, right)

#this problem can be solved using merge sort algorithm. The function sortArray takes a list of integers as input and returns a sorted list of integers. It uses a recursive approach to divide the input list into smaller sublists until the base case is reached (when the length of the list is less than or equal to 1). Then, it merges the sorted sublists back together using the merge function, which compares elements from both sublists and appends them in sorted order to a new list. Finally, the sorted list is returned.