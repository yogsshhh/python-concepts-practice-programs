1. add the inbetween numbers

s="asv234ad43aegra3va34ag33"
res=0
nums=""
for i in s:
    if i.isdigit():
        nums+=i
    else:
        if nums:
            res+=int(nums)
            nums=""
if nums:
    res+=int(nums)
print(res)

