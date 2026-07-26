class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = sum(accounts[0])
        for customer in accounts:
            if sum(customer) > richest:
                richest = sum(customer)
        return richest

#This problem can be solved in O(n*m) time complexity, where n is the number of customers and m is the number of accounts per customer. We iterate through each customer's account list, calculate the total wealth by summing the values in their account list, and keep track of the maximum wealth encountered. Finally, we return the maximum wealth found among all customers.