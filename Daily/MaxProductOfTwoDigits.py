class Solution:
    def maxProduct(self, n: int) -> int:
        m1 = 0
        m2 = 0
        while n > 0:
            d = n % 10
            if d > m1:
                m2 = m1
                m1 = d
            elif d > m2:
                m2 = d
            n //= 10
        return m1 * m2

#this problem can be solved in O(log n) time complexity by iterating through the digits of the input number. We maintain two variables, m1 and m2, to keep track of the two largest digits we have seen so far. For each digit, we compare it with m1 and m2 and update them accordingly. Finally, we return the product of m1 and m2, which represents the maximum product of two digits in the input number.