class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = s[::-1]
        if s == r:
            return True
        else:
            return False

#this problem can be solved in O(n) time complexity, where n is the number of digits in the input integer. We convert the integer to a string, reverse the string, and compare it with the original string. If they are equal, the integer is a palindrome; otherwise, it is not.