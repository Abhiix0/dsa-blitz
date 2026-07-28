from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        total_sum = 0
        count = Counter(nums)
        
        for num, val in count.items():
            if val == 1:
                total_sum += num
                
        return total_sum

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We use a Counter to count the occurrences of each number in the input list. We then iterate through the items in the Counter, checking if the count of each number is equal to 1 (indicating it is unique). If it is unique, we add it to a running total. Finally, we return the total sum of unique elements.