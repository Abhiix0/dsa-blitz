class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        current = 0
        minimum = 0

        for num in nums:
            current += num
            minimum = min(minimum, current)

        return 1 - minimum

#this problem can be solved in O(n) time complexity, where n is the length of the input list. We maintain a running sum of the elements in the list and keep track of the minimum value encountered during this process. The minimum starting value required to ensure that the running sum never drops below 1 is calculated as 1 minus the minimum value found.


'''
Without min()
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current = 0
        minimum = 0

        for num in nums:
            current += num

            if current < minimum:
                minimum = current

        return 1 - minimum
'''