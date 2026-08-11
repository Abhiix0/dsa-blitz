class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        seen = set(nums)
        candidate = total

        while candidate in seen:
            candidate += 1

        return candidate

#this problem can be solved in O(n) time complexity, where n is the length of the input list. We first calculate the total sum of the consecutive integers starting from the first element. Then, we use a set to keep track of the seen integers and find the smallest missing integer by incrementing a candidate value until it is not found in the set.