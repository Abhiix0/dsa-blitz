class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = 0
        right = 0
        cut = 0

        for ch in s:
            if ch == 'L':
                left += 1
            if ch == 'R':
                right += 1

            if left == right:
                cut += 1

        return cut

#This problem can be solved in O(n) time complexity, where n is the length of the input string. We iterate through the string and maintain two counters for 'L' and 'R'. Whenever the counts of 'L' and 'R' are equal, we increment the cut counter. Finally, we return the total number of cuts made.