class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        M = None
        for num in nums:
            if count == 0:
                M = num
            if M == num:
                count += 1
            elif M != num:
                count -= 1
        return M

#this problem can be solved in O(n) time complexity by using the Boyer-Moore Voting Algorithm. The idea is to maintain a count variable and a candidate variable (M) for the majority element. We iterate through the input list and for each number, we check if the count is zero. If it is, we set the candidate to the current number. Then, we compare the current number with the candidate. If they are the same, we increment the count; if they are different, we decrement the count. By the end of the iteration, the candidate will be the majority element, which we return.