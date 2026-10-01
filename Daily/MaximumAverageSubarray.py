class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        end = k
        window_sum = 0

        for num in nums[start:end]:
            window_sum += num
        max_sum = window_sum

        while end<len(nums):
            window_sum -= nums[start]
            window_sum += nums[end]

            max_sum = max(max_sum, window_sum)
            start += 1
            end += 1
        return float(max_sum/k)

#this problem can be solved using sliding window approach. We can start with a window of size k and calculate the sum of the first k elements. We then slide the window one element at a time, subtracting the element that is leaving the window and adding the element that is entering the window. We keep track of the maximum sum we have seen so far and return the average of that maximum sum divided by k at the end.