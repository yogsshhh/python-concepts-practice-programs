

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

