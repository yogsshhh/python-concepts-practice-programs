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

# Model: Work with consecutive characters in a string.

# Q: Print all substrings of "abc".
# Input: "abc"
# Output:

# a
# ab
# abc
# b
# bc
# c
    
n="abcd"
for i in range(len(n)):
    for j in range(i,len(n)):
        sub=n[i:j+1]
        print(sub)
#  Substring with Fixed Length

# Model: Substring of specific size k.

# Q: Print all substrings of length 2.
# Input: "abcd"
# Output:

# ab
# bc
# cd

n="abcd"
k=2
for i in range(len(n)-k+1):
    sub=n[i:i+k]
    print(sub)

# Longest Consecutive Substring (Character-based)

# Model: Find longest substring satisfying some property.

# Q: Longest substring with all distinct characters.
# Input: "abcabcbb"
# Output: 3
# Explanation: Longest substring = "abc" → length = 3.

n="abcdabacg"
c=1
con=[]
for i in range(len(n)-1):
    if ord(n[i+1]) - ord(n[i]) == 1:
        c+=1
    else:
        con.append(c)
        c=1
con.append(c)
print(max(con))

