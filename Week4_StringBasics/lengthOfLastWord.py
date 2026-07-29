class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

#This problem can be solved in O(n) time complexity, where n is the length of the input string. We split the string into words using the split() method, which handles multiple spaces and trims leading/trailing spaces. We then access the last word in the resulting list and return its length using the len() function.

#class Solution:
#    def lengthOfLastWord(self, s: str) -> int:
#        i = len(s) - 1
#       while i >= 0 and s[i] == " ":
#           i -= 1
#      length = 0
#      while i >= 0 and s[i] != " ":
#          length += 1
#          i -= 1
#      return length