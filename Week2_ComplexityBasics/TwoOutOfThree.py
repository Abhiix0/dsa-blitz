class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        
        a = s1 & s2
        b = s2 & s3
        c = s1 & s3
        
        result = a | b | c
        
        return list(result)

#this problem can be solved in O(n) time complexity by using sets to store the unique elements of each input list. We first convert each list into a set to eliminate duplicates. Then, we find the intersection of each pair of sets (s1 & s2, s2 & s3, s1 & s3) to identify the common elements between the lists. Finally, we take the union of these intersections to get the final result containing elements that appear in at least two of the three input lists. The result is then converted back to a list and returned.