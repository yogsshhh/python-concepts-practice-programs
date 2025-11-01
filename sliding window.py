-----SLIDING WINDOW
-------------SHRINK WINDOW/RESET POINTER BY RULES

1.lenght of longest substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxi = max(maxi, right - left + 1)

        return maxi
