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



# Count subarrays with product < K
# Input: [10,5,2,6], K=100
# Output: 8

arr=[10,5,2,6]
k=100
prod=1
left=0
count=0
for right in range(len(arr)):
    prod*=arr[right]
    
    
    while prod >=k and left <right:
        prod//= arr[left]
        left+=1
        
    count+=(right-left+1)
print(count)


# Maximum product subarray
# Input: [2,3,−2,4]
arr=[2,3,-2,4]   

max_prod=arr[0]
min_prod=arr[0]
ans=arr[0]


for i in arr[1:]:
    if i<0:
        max_prod,min_prod=min_prod,max_prod
        
    max_prod=max(i,max_prod*i)
    min_prod=min(i,max_prod)
    
    ans=max(max_prod,ans)




































































































































