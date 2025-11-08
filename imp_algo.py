# kadne's algorithm maximum sum of subarray
arr = [-2,1,-3,4,-1,2,1,-5,4]

max_ending = max_so_far = arr[0]

for x in arr[1:]:
    max_ending = max(x, max_ending + x)
    max_so_far = max(max_so_far, max_ending)

print(max_so_far)


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
