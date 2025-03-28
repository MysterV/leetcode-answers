# maybe not the fastest, but it gets the job done, and beats up to 99.6% alternatives in terms of memory
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        for i in range(len(s)):
            found = set()
            if max_l >= len(s)-i: break
            for j in range(i, len(s)):
                if s[j] in found: break
                else: found.add(s[j])
            if len(found) > max_l:
                max_l = len(found)
        return max_l