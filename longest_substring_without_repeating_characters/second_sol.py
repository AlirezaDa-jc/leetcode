class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        charMap = {}
        maxLen = 0
        left = 0
        for i, ch in enumerate(s):
            if ch in charMap and charMap[ch] >= left:
                left = charMap[ch] + 1
            charMap[ch] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen
