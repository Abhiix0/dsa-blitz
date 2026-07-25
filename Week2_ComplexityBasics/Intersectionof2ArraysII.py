class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        r = {}
        for num in nums1:
            r[num] = r.get(num,0) + 1
        res = []
        for num in nums2:
            if num in r and r[num] > 0:
                res.append(num)
                r[num] -= 1
        return res

#this problem can be solved in O(m + n) time complexity by using a hash map to store the frequency of elements in one array and then iterating through the other array to find the common elements. Here, m and n are the lengths of the two input arrays. We first create a hash map to count the occurrences of each element in the first array. Then, we iterate through the second array and check if each element exists in the hash map with a positive count. If it does, we add it to the result list and decrement its count in the hash map. Finally, we return the result list containing the intersection of the two arrays.