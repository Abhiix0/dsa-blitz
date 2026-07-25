class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
       n = len(nums)
       result = []
       checklist = [False] * (n+1) 
       for num in nums:
         checklist[num] = True
        
       for i in range(1, n + 1):
         if checklist[i] == False:
            result.append(i)
                
       return result

#this problem can be solved in O(n) time complexity by using a checklist array to keep track of the numbers that are present in the input list. We first create a checklist array of size n+1 initialized to False. Then, we iterate through the input list and mark the corresponding index in the checklist as True for each number found. After that, we iterate through the checklist from index 1 to n and collect the indices that are still marked as False, which represent the disappeared numbers. Finally, we return the list of disappeared numbers.