class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write
# This problem can be solved in O(n) time complexity, where n is the length of the input array. We use a two-pointer approach, where one pointer (write) keeps track of the position to write the next non-val element, and the other pointer iterates through the array. If the current element is not equal to val, we write it to the position indicated by the write pointer and increment the write pointer. Finally, we return the value of the write pointer, which represents the new length of the array after removing all instances of val.