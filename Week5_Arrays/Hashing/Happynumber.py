class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()   
        while n not in s:    
            s.add(n)  
            sum = 0  
            while n > 0:  
                r = n%10      
                sum += r**2   
                n = n // 10     
            if sum == 1:   
                return True   
            else:    
                n = sum    
        return False 

#this problem can be solved using a set data structure. The function isHappy takes an integer n as input and returns a boolean indicating whether n is a happy number. It uses a set s to keep track of the numbers encountered during the process. The function repeatedly calculates the sum of the squares of the digits of n until either n becomes 1 (indicating it is a happy number) or n is found in the set (indicating it is not a happy number). If n becomes 1, the function returns True; otherwise, it returns False when a cycle is detected.