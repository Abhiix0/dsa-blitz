class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        r = 0
        a = []
        for num in gain:
            r += num
            a.append(r)
        if max(a) < 0:
            return 0    
        return max(a)

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We maintain a variable r to keep track of the current altitude and a list a to store the altitudes at each step. We iterate through the gain list, updating r by adding the current gain value and appending the new altitude to the list a. After processing all gain values, we check if the maximum altitude in a is less than 0; if it is, we return 0 as the highest altitude. Otherwise, we return the maximum value from the list a as the result.