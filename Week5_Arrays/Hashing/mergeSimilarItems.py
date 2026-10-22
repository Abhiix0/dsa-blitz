class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        h = {}
        for k,v in items1:
            h[k] = h.get(k,0) + v
        for k,v in items2:
            h[k] = h.get(k,0) + v
        return [[v,k] for v,k in sorted(list(h.items()))]

#this problem can be solved using the hashmap data structure. The function mergeSimilarItems takes two lists of items as input, where each item is represented by a list of two integers (the value and the weight). It uses a dictionary h to accumulate the weights for each unique value from both input lists. The function iterates through each item in items1 and items2, updating the dictionary with the total weight for each value. Finally, it returns a sorted list of lists, where each inner list contains the value and its corresponding total weight.