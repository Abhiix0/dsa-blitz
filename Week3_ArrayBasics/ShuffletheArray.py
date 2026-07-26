class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        r = []
        for i in range(n):
            r.append(nums[i])
            r.append(nums[i + n])
        return r

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We iterate through the first half of the input list and for each index, we append the corresponding elements from both halves of the list to a new list. Finally, we return the new list containing the shuffled elements.