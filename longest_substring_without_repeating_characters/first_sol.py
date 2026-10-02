class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxLen = 1
        sub = s[0]
        for ch in s[1:]:
            if ch not in sub:
                sub = sub + ch
                if len(sub) > maxLen:
                    maxLen = sub
            else:
                sub = sub[sub.index(ch) + 1 :] + ch
        return maxLen
