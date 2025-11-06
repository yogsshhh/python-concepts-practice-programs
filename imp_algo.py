# kadne's algorithm maximum sum of subarray
arr = [-2,1,-3,4,-1,2,1,-5,4]

max_ending = max_so_far = arr[0]

for x in arr[1:]:
    max_ending = max(x, max_ending + x)
    max_so_far = max(max_so_far, max_ending)

print(max_so_far)
