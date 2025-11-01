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

# 2.Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead
#     .
# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mini=float('inf')
        curr_sum=0
        for right in range(len(nums)):
            curr_sum+=nums[right]

            while curr_sum >=target:
                mini=min(mini,right-left+1)
                curr_sum-=nums[left]
                left+=1
        return 0 if mini==float('inf') else mini



3.Longest Substring with At Most K Distinct Characters







































































































































