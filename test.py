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



s = "listen"
t = "silent"

d1 = {}
d2 = {}

for ch in s:
    d1[ch] = d1.get(ch, 0) + 1

for ch in t:
    d2[ch] = d2.get(ch, 0) + 1

print(d1 == d2)




from collections import Counter

s = "listen"
t = "silent"

print(Counter(s) == Counter(t))



# 2.Alex Gives You a positive Number N and wants you to rearrange the
# bits of the number in its binary representation such that all set bits are in consecutive order. 
# Your task is to find and return an integer value representing the minimum possible number that can be formed after re-arranging the bits of the number N.

# Example

# Input1: 10      
# Output: 3
# Explanation: 10 -> binary: 1010 count the set bits and arrange in consecutive order such as 0011 which in decimal is 3.

# Input: 2
# Output: 1



n=10
ze,o="",""
bi=bin(n)[2:]

for i in bi:
    if i == "0":
        ze+=i
    else:
        o+=i
r=ze+o
ss=int(r,2)
print(ss)


# 4.Problem Statement 

# You are provided with a string which has a sequence of 1s and Os. This sequence is the encoded version of a english word. You are supposed to write a program 
# to decode the provided string and find the original word. Each uppercase Alphabet is representing by a sequence of 1s

# Input: 10110111
# Output: ABC

s="10110111".split("0")
p=""
res=""
for i in s:
    length=len(i)
    res+=chr(ord("A")+length-1)
print(res)

s="abac"
d={}
for i in s:
    val= ord(i)-ord('a')+1
    
    d[val]=d.get(val,0)+1
sums=sum(i for i ,j in d.items() if j==1)
print(sums)






