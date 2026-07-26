class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        profit = 0
        for num in prices:
            if num < low:
                low = num
            tp = num - low
            if tp > profit:
                profit = tp
        return profit

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We maintain a variable (low) to track the minimum price encountered so far and a variable (profit) to track the maximum profit. We iterate through the list of prices, updating the low price when we find a new minimum and calculating the potential profit for each price. If the potential profit exceeds the current maximum profit, we update the profit variable. Finally, we return the maximum profit found.