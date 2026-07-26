class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2

        count = 0

        for item in items:
            if item[index] == ruleValue:
                count += 1

        return count

#This problem can be solved in O(n) time complexity, where n is the number of items in the input list. We first determine the index corresponding to the ruleKey (0 for "type", 1 for "color", and 2 for "name"). We then iterate through each item in the items list and check if the value at the determined index matches the ruleValue. If it does, we increment a count variable. Finally, we return the count of matching items.