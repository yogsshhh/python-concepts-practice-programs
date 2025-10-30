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
































































