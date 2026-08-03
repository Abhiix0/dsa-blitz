class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ref = strs[0]
        r = ""
        for i in range(len(ref)):
            for ch in strs[1:]:
                 if len(ch) <= i or ch[i] != ref[i]:
                    return r

            r += ref[i]
        return r

#this program is to find the longest common prefix in a list of strings. It takes the first string as a reference and compares each character with the corresponding characters in the other strings. If a mismatch is found or if any string is shorter than the current index, it returns the accumulated prefix. If all characters match, it continues to build the prefix until the end of the reference string.