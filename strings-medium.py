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


2.number betweeen alphabets

a="a123bc34d5s7er"
c=0
temp=''
for i in a:
    if i.isdigit():
        temp+=i
    else:
        if temp!='':
            c+=1
            temp=""
print(c)

3. even odd frequencyy

a="asdfessjj"
d={}
ev=0
od=0
for i in a:
    d[i]=d.get(i,0)+1
for i,j in d.items():
    if j %2 ==0:
        ev+=1
    else:
        od+=1
print(abs(ev-od))


4.# I/p:sandhiya
# O/p: SaNdHiYa


s="sandhiya"
res=""
for i in range(len(s)):
    if i%2==0:
        res+=(s[i].upper())
    else:
        res+=(s[i].lower())
print(res)

# 5.
# i/p:hel233o2Worl4d
# O/p:heloWorld


s='hel234oWo423rld'
res=""
for i in s:
    if i.isalpha():
        res+=i
print(res)

# 6.
# I/p:banana
# O/p:a3b1n2

s="banana"
S=sorted(s)
res=""
d={}
for i in S:
    d[i]=d.get(i,0)+1
for i,j in d.items():
    res+=i
    res+=str(j)
print(res)


# 5
# I/p:s1:abc
#       S2:xyzgf

# O/p:axbyczgf
s1,s2='abc','xyzgf'
res=""
for i in range(min(len(s1),len(s2))):
    res+=s1[i]
    res+=s2[i]
res += s1[min(len(s1), len(s2)):]
res += s2[min(len(s1), len(s2)):]
print(res)

# keyboar keys problem
s="ajiiikalamaass"
res=""
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        res+=s[i-1]
res+=s[-1]
print(res)


# 1. Replace Characters in a String
# Input:
# Str: apples
# ch1: a
# ch2: p

# Output: paales
s="apples"
ch1='a'
ch2='p'
temp="#"
s=s.replace(ch1,temp)
s=s.replace(ch2,ch1)
s=s.replace(temp,ch2)
print(s)


# 2. Shorten Word with Middle Character Count
# Input:
# examination

# Output:
# e9n

s = input("Enter a word: ")
if len(s) <= 2:
    print(s)
else:
    print(s[0] + str(len(s) - 2) + s[-1])


# 1️⃣ Swap Case of Vowels Only

# Input:
# s = "Accenture"
# Output:
# aCCEntUrE
# Hint: If it’s a vowel → swap its case; else keep as is


s="accenture"
vow="aeiouAEIOU"
res=""
for i in range(len(s)):
    if s[i] in vow:
        if s[i].isupper():
            res+=s[i].lower()
        else:
            res+=s[i].upper()
    else:
        res+=s[i]
print(res)


# 2️⃣ Reverse Every Word Except the First and Last

# Input:
# s = "Python is very interesting"
# Output:
# Python si yrev interesting
# Hint: Split, loop, reverse only middle words.

s="python is very intresting"
s=s.split()
f=s[0]
l=s[-1]
res=[]
for i in range(1,len(s)-1):
    res.append(s[i][::-1])
print(f," ".join(res),l)


























































