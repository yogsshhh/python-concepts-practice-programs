# Program 10 - Email ID Obfuscation (Category: Difficult)
# Personal information like email id and other contact details need to be handled in a way so that privacy of the user is safeguarded. One way to do this is to hide or partially hide such information, also called obfuscation of the information.
# Given the email id as input, the program should obfuscate the id as follows:
# 1) For the given mail id, the part that comes before @ is referred to as the first part. If there is no first @ character, the mail id is invalid.
# 2) If the first part of the email id is less than or equal to 5 characters in length, replace all characters in the first part with *
# 3) If the first of the email id is greater than 5 characters in length, print the first 3 characters as it is and replace the remaining characters of the first part with *
# 4) If the email id is invalid, print Invalid Input.
# Example 1:
# Input:
# abc@gmail.com
# Output:
# ***@gmail.com


n=input().split("@")
re=''
r=''
if len(n) <2:
    print("Invalid")
else:
    if len(first) <= 5:
        re = '*' * len(first)
    else:
        re = first[:3] + '*' * (len(first) - 3)
    
print(re + '@' + domain)

# Program 2: Table of Numbers
# Write a program to display the table of a number and print the sum of all the multiples in it.
# L
# Case 1
# Input (stdin)
# 12
# Output (stdout)
# 12 24 36 48 60 72 84 96 108

# 660


n=12
sums=0
fi=[]
for i in range(1,11):
    res=i*n
    fi.append(res)
    sums+=res
print(*fi)
print(sums)

# Program 3
# Instructions: You are required to write the code. You can click on compile and run anytime to check compilation/execution status. The code should be logically/syntactically correct.
# Question: Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate pallindrome numbers.
# TestCase 1:
# Input:
# 10,80
# Expected Result:
# 11,22,33, 44, 55, 66, 77.
# Test Case 2:
# Input:
# 100,200
# Expected Result:
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191.

def palindrome(n):
    rev = 0
    temp=n
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    if temp==rev:
        return "yes"
    else:
        return "no"
res=[]

# most reapting letter in a word

n="happyending"
d={}
for i in n:
    d[i]=d.get(i,0)+1
res=max(d.values())
for i,j in d.items():
    if res==j:
        print(i)
        break


# Program 6: Integer Difference
# Given an array arr and two integer value n and m as input, take the first element and find the difference between the first element and the integer value n. If the difference is less than m then increment that particular array element. Do this for all the element in an array and print the final modified array as output.
# Sample Input:
# 5 21457 32
# Sample Output: 32557

arr = [2, 3, 5, 7, 3, 5]
n = 5
m = 3   # threshold

first = arr[0]

for i in range(len(arr)):
    if abs(arr[i] - first) < m:   # difference with first element
        arr[i] += 1

print(arr)



































































