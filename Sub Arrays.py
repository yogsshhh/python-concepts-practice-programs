# 🧩 3️⃣ Subarray with Specific (Fixed) Size

# Model: Find a subarray of size K satisfying a condition.

# Q: Find the maximum sum subarray of size 3.
# Input: arr = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: Subarray [5, 1, 3] → sum = 9 (maximum among all subarray).

arr=[2, 1, 5, 1, 3, 2]
k=3
big=0
temp=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        sub=arr[i:j+1]
        if len(sub) ==k:
            temp=sum(sub)
        if temp > big:
            big=temp
print(big)
----------------------------------
arr=[2, 1, 5, 1, 3, 2]
k=3
big=0
for i in range(len(arr)-k+1):
        sub=sum(arr[i:k+1])
        if sub > big:
            big=sub
print(big)

# 🧩 5️⃣ Subarray — All Pairs (2-element subarray)

# Model: Work with pairs of elements (subarrays of size 2).

# Q: Print all pairs and their sums.
# Input: arr = [4, 7, 1]
# Output:

# Pairs: (4,7), (4,1), (7,1)
# Sums: 11, 5, 8

from itertools import combinations
arr = [4, 7, 1]
comb=list(combinations(arr,2))
sums=[]
for i in comb:
    k=sum(i)
    sums.append(k)
print(*comb)
print(*sums)


# Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices 
# such that the sum of their elements is equal to the target

#     .

# Examples:

# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: arr[3] + arr[4] = -3 + 1 = -2
# Input: arr[] = [1, -2, 1, 0, 5], target = 0
# Output: false
# Explanation: None of the pair makes a sum of 0

s=set()
	    for i in arr:
	        if target-i in s:
	            return True
	        s.add(i)
	    return False
	---------------------------------

arr.sort()
	    l,r=0,len(arr)-1
	    while l <r:
	        s=arr[l]+arr[r]
	        if s==target:
	            return True
	        elif s < target:
	            l+=1
	        else:
	            r-=1
	    return False
	        

# 12. Longest consecutive subarray
# Input: [2,3,4,7,8,9,10]
# Output: Longest length=4 (subarray [7,8,9,10])


arr=[2,3,4,7,8,9,10,11]
res=[]
c=1
for i in range(len(arr)-1):
    if arr[i]+1 ==arr[i+1]:
        # res.append(i)
        c+=1
    else:
        res.append(c)
        c=1
res.append(c)
print(max(res))

























