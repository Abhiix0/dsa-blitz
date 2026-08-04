class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            i -= 1
            j -= 1
            
        return "".join(res[::-1])

#this problem can be solved in O(max(n, m)) time complexity, where n and m are the lengths of the input strings num1 and num2 respectively. We iterate through both strings from the end to the beginning, adding corresponding digits along with any carry from the previous addition. We use the ord() function to convert characters to their integer values. The result is built in reverse order and then reversed before returning as a string.