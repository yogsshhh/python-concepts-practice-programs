🧩 3️⃣ Subarray with Specific (Fixed) Size

Model: Find a subarray of size K satisfying a condition.

Q: Find the maximum sum subarray of size 3.
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5, 1, 3] → sum = 9 (maximum among all subarray).

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
