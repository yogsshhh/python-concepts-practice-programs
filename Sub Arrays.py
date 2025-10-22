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

