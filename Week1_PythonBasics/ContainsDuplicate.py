class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

#this problem can be solved in O(n) time complexity by using a hash set to keep track of the numbers we have seen so far. We iterate through the input list and for each number, we check if it is already present in the hash set. If it is, we return True, indicating that there is a duplicate. If not, we add the number to the hash set and continue iterating. If we finish iterating through the list without finding any duplicates, we return False.