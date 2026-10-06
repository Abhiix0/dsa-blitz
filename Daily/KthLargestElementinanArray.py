import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

#this problem can be solved using a min-heap data structure. The function findKthLargest takes a list of integers and an integer k as input and returns the kth largest element in the list. It iterates through each number in the input list, pushing it onto the heap. If the size of the heap exceeds k, it pops the smallest element from the heap. After processing all elements, the smallest element in the heap (which is at index 0) will be the kth largest element in the original list, and it is returned as the result.