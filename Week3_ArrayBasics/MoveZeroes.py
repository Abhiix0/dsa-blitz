class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        for i in range(insert,len(nums)):
            nums[i] = 0
        

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We maintain a pointer (insert) to track the position where the next non-zero element should be placed. We iterate through the input list and for each non-zero element, we place it at the insert position and increment the insert pointer. After processing all elements, we fill the remaining positions in the list with zeros. This way, we move all zeros to the end while maintaining the relative order of non-zero elements.