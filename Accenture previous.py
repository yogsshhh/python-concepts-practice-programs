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

#rev a number and palindrome

n = int(input("Enter a number: "))
temp = n     # store original number
rev = 0      # reversed number

while n > 0:
    digit = n % 10          # get last digit
    rev = rev * 10 + digit  # add it to reverse
    n = n // 10             # remove last digit

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#  greatest of three numbers
n1=int(input())
n2=int(input())        
n3=int(input())
if n1 >= n2 and n1 >= n3:
    print("num 1 is larger")
elif n2 >=n1 and n2 >=n3:
    print(("num 2 is larger"))
else:
    print("num 3 is larger")

# You are given two strings, s and t . Your task is to determine if it's
# possible to rearrange the characters of s to form the string t .
# Write a function that returns True it's possible to create t by
# rearranging the characters of s and False otherwise.
# Input
# Two strings, s and t where the length of s and t are between 1 and
# 1000 characters.
# Output
# Return True if it's possible to create t by rearranging the characters of
# s and False otherwise
# Example:
# s="listen"
# t="silent"
# Output:
# True/

s="listen"
t="silent"
d1={}
d2={}
for i in s:
    d1[i]=d1.get(i,0)+1
for i in t:
    d2[i]=d2.get(i,0)+1
if d1==d2:
    print(True)
    
else:
    print(False)

# A single line of text containing words separated by spaces. The input
# string consists of only printable ASCII characters.
# Output:
# The string with words reversed in order.
# Example:
# Input:
# Hello World
# Output:
# World Hello

n="Hell NO"
n=n.split()
r=len(n)-1
res=[]
while r >=0 :
    res.append(n[r])
    r-=1
print(" ".join(res))
-----------------------------------------------

print(" ".join(n.split()[::-1]))


# You are given an integer 'n'
# . Write a Python function to calculate and
# return the sum of the digits in 'n' after converting it to its binary
# representation.
# For example, 15, which has a binary representation of 1111, should
# return 4.


n=15
r=bin(n)
arr=r[2:]
sums=0
for i in arr:
    sums+=int(i)
print(sums)
--------------------------------------
print(sum(int(i) for i in bin(n)[2:]))


# Write the Python function sumevenandodd(arr) to solve this problem.
# The function should take an array of integers as input and return a
# tuple of two integers the first element being the sum of even numbers,
# and the second element being the sum of odd numbers

arr=[1,2,3,4,5,6,7]
e=0
o=0
for i in arr:
    if i&1:
        o+=i
    else:
        e+=i
print((e,o))

# You have been given an integer N as input . your task is to write a
# program to print N rows of Floyad’s Triangle. Floyd's pattern is a rightangled triangular array of natural numbers , used for the numbering of
# lines in a printout
# .
# For N=4,
# 1
# 23
# 456
# 78910

n=int(input())
for i in range(n):
    for j in range(i):
        print(i,end="")
        i+=1
    print()

# Rohan is a kid who has just learned about creating words from
# alphabets. He has written some words in the notepad of his Father
# laptop. Now his father wants to find the longest word written by Rohan
# using a computer program. Write a program to find the longest string
# in a given list of strings.
# Example:
# Input: yes no number
# Output: The longest string is: number


n=input().split()
max=0
r=""
for i in range(len(n)):
    temp=len(n[i])
    if temp>max:
        r=n[i]
        max=temp
print(r)    


number betweeen alphabets

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






























































