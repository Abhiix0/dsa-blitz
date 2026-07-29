class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for ch in address:
            if ch == '.':
                result += '[.]'
            else:
                result += ch

        return result

#address.replace(".", "[.]") : this works too, but the above solution is more efficient as it avoids creating multiple intermediate strings.
#This problem can be solved in O(n) time complexity, where n is the length of the input string. We iterate through the string and check each character. If the character is a dot ('.'), we append '[.]' to the result string; otherwise, we append the character itself. Finally, we return the modified result string.