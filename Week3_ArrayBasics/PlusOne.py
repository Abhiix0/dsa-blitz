class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

#This problem can be solved in O(n) time complexity, where n is the length of the input list. We iterate through the list of digits from the last digit to the first digit. If we encounter a digit that is not 9, we simply increment that digit by 1 and return the modified list. If we encounter a 9, we set it to 0 and continue to the next digit. If all digits are 9, we return a new list with a leading 1 followed by n zeros, where n is the length of the original list. This handles the case where an additional digit is needed (e.g., going from 999 to 1000).