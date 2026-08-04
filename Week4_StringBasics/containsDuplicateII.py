class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):

            if nums[i] in seen:

                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We use a dictionary to keep track of the indices of the numbers we have seen so far. As we iterate through the list, we check if the current number has been seen before and if the difference between the current index and the index of the last occurrence is less than or equal to k. If both conditions are met, we return True, indicating that there is a nearby duplicate. If we finish iterating through the list without finding any nearby duplicates, we return False.