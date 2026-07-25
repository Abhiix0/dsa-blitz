class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

#this problem can be solved in O(n) time complexity by iterating through the stones string and checking if each stone is present in the jewels string. We maintain a count variable to keep track of the number of stones that are also jewels. For each stone, if it is found in the jewels string, we increment the count. Finally, we return the total count of jewels found in the stones.