from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        if k == 0:
            return

        last = nums[-k:]
        first = nums[:-k]

        nums[:] = last + first

# This problem can be solved in O(n) time complexity, where n is the length of the input array. We first calculate the effective number of rotations needed by taking k modulo the length of the array. If k is zero, we return early as no rotation is needed. We then split the array into two parts: the last k elements and the first n-k elements. Finally, we concatenate these two parts in reverse order and update the original array in place using slicing.

'''
Repeated rotation:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)
'''

'''
New array + index mapping
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        result = [0] * n

        for i in range(n):
            new_index = (i + k) % n
            result[new_index] = nums[i]

        nums[:] = result
'''