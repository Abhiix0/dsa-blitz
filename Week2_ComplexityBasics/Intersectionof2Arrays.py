class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        r = set()
                
        for num in nums2:
            if num in set1:
                r.add(num) 
                        
        return list(r)    

#this problem can be solved in O(m + n) time complexity by using a hash set to store the elements of one array and then iterating through the other array to find the common elements. Here, m and n are the lengths of the two input arrays.