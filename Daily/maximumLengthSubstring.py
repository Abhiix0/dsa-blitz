class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        count = {}
        maximum = 0

        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1

            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum

# This problem can be solved in O(n) time complexity, where n is the length of the string. We use a sliding window approach to maintain a substring with at most two occurrences of each character. By expanding the right pointer and adjusting the left pointer when necessary, we can efficiently find the maximum length of such a substring.