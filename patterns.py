
1
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 

n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

2
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 

n=8
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()



3
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

n=8
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

4
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********

n=8
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

5
 *******
  ******
   *****
    ****
     ***
      **
       *
        

n=8
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    print()


6
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
  * * * * * * * 
 * * * * * * * * 

n=8
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")


7

* * * * * * * * 
  * * * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()


8

        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
  * * * * * * * 
 * * * * * * * * 
 * * * * * * * * 
  * * * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 

n=8
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print() 







----------------------------------------------------NUMBER PATTERN------------------------------------------------


1
11
111
1111
11111
111111
1111111


n=8
for i in range(n):
    for j in range(i+1):
        print(1,end="")
    print()

1
22
333
4444
55555

n=5
r=1
for i in range(n):
    for j in range(i+1):
        print(r,end="")
    r+=1
    print()

5
44
333
2222
11111

n=5
r=5
for i in range(n):
    for j in range(i+1):
        print(r,end="")
    r-=1
    print()

0
22
444
6666
88888

n=5
r=0
for i in range(n):
    for j in range(i+1):
        print(r,end="")
    r+=2
    print()

1
22
111
2222
11111


n=5
for i in range(n):
    for j in range(i+1):
        if i&1==0:
            print(1,end="")
        else:
            print(2,end="")
    print()



     1 
    2 2 
   3 3 3 
  4 4 4 4 
 5 5 5 5 5
  4 4 4 4 
   3 3 3 
    2 2 
     1 


n=5
r=1

for i in range(n):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i + 1):
        print(r, end=" ")
    r += 1
    print()
p = n-1
for i in range(1,n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i, n):
        print(p, end=" ")
    p -= 1
    print()


1
12
123
1234
12345

n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end="")
        p+=1
    print()


     5
    54
   543
  5432
 54321

n=5
for i in range(n):
    p=5
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print(p,end="")
        p-=1
    print()


         1 
        1 2 
       1 2 3 
      1 2 3 4 
     1 2 3 4 5 
    1 2 3 4 5 6 
   1 2 3 4 5 6 7 
  1 2 3 4 5 6 7 8 
 1 2 3 4 5 6 7 8 9 

n=9
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()


     1 
    1 2 1 
   1 2 3 2 1 
  1 2 3 4 3 2 1 
 1 2 3 4 5 4 3 2 1 




n=5
p=1
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end=" ")
        p+=1
    for j in range(i+1):
        print(p,end=" ")
        p-=1
    print()




































