1# Count Magical Numbers
# Input: [10, 12, 15, 19]
# Output: 1
# Explanation: Magical numbers are those whose sum of digits is divisible by 5.


arr=[10,12,15,19]
c=0
res=0
for i in arr:
    res=0
    while i >0:
        res+=i%10
        i=i//10
    if res%5==0:
        c+=1
print(c)

# Sum of Primes
# Input: [1, 2, 3, 4, 5, 6]
# Output: 10
# Explanation: 2 + 3 + 5 = 10.

def prime(n):
    if n >1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False

n=[1,2,3,4,5,6]
res=0
for i in n:
    if prime(i) == True:
        res+=i
print(res)

# Negative Growth
# Input: [10, 9, 8, 12, 11]
# Output: 3
# Explanation: Three times value decreases compared to previous.

arr=[10,9,8,12,11]
maxi=1
c=1
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        c+=1
    else:
        maxi=max(maxi,c)
        c=1
maxi=max(maxi,c)
print(maxi)

# Multiple of Three
# Input: [3, 4, 9, 12]
# Output: 3
# Explanation: 3, 9, 12 are multiples of 3.

arr=[3,4,9,12]
c=0
for i in arr:
    if i %3 ==0:
        c+=1
print(c)

# Prime Sum
# Input: 10
# Output: 17
# Explanation: Sum of primes till 10 = 2 + 3 + 5 + 7 = 17

n=10
def prime(n):
    if n >1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

n=10
res=0
for i in range(n+1):
    if prime(i)==True:
        res+=i
print(res)

# Area of Canopy
# Input: r = 5
# Output: 78.5
# Explanation: Area = π * r^2.

r=5
print(3.14*(r**2))

# Prime Sum
# Input: 10
# Output: 17
# Explanation: Sum of primes till 10 = 2 + 3 + 5 + 7 = 17


def prime(n):
    if n >1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def rev(n):
    rev=0
    while n > 0:
        digit = n % 10          # get last digit
        rev = rev * 10 + digit  # add it to reverse
        n = n // 10 
    if prime(rev) == True:
        return True
n=13
if prime(n) == True and rev(n) ==True:
    print("True")
else:
    print("False")


































































