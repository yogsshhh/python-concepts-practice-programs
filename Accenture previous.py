Program 10 - Email ID Obfuscation (Category: Difficult)
Personal information like email id and other contact details need to be handled in a way so that privacy of the user is safeguarded. One way to do this is to hide or partially hide such information, also called obfuscation of the information.
Given the email id as input, the program should obfuscate the id as follows:
1) For the given mail id, the part that comes before @ is referred to as the first part. If there is no first @ character, the mail id is invalid.
2) If the first part of the email id is less than or equal to 5 characters in length, replace all characters in the first part with *
3) If the first of the email id is greater than 5 characters in length, print the first 3 characters as it is and replace the remaining characters of the first part with *
4) If the email id is invalid, print Invalid Input.
Example 1:
Input:
abc@gmail.com
Output:
***@gmail.com


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
