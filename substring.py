

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


# 🧩 9️⃣ All Possible Substrings (Brute Force)

# Model: Generate every substring.

# Q: Print all possible substrings.
# Input: "xy"
# Output:

# x
# xy
# y
n = "san"

for i in range(len(n)):         
    for j in range(i, len(n)):  
        print(n[i:j+1]) 


# 2. Longest Substring With Same Character

# Input: "aaabbbaaac"
# Output: 3
# Explanation: "aaa" or "bbb".


s="aaaaaaaaaabbbbccccccccccccccccccccccc"
c=1
max_len=1
for i in range(1,len(s)):
    if s[i] ==s[i-1]:
        c+=1
    else:
        max_len=max(c,max_len)
        c=1
max_len=max(c,max_len)
print(max_len)































