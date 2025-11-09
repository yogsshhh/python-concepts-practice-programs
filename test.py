# findCount Function
# Implement:
# int findCount(int arr[], int length, int num, int diff)
# Return how many elements in arr have absolute difference ≤ diff from num.
# If none, return -1.

# Example:
# arr = {12,3,14,56,77,13}, num = 13, diff = 2 → Output: 3


arr = [12,3,14,56,77,13]
num = 13
diff = 2
c=0   
for i in arr:
    if abs(i-num) >= 2:
        c+=1
        
print(c)


























