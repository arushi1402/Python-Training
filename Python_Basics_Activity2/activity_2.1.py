#1
num= int(input("Enter Number : "))
if num > 0:
    print("This is a positive number")
else:
    print("This is a negative number")
    

#2
n= int(input("Enter Number : "))
if (n % 2) == 0:
    print("This is a even number")
else:
    print("This is a odd number")

#3
year=int(input("Enter Number : "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"is a leap year")
else:
    print( year,"is not a leap year")

#4
a=int(input("Enter Number : "))
b=int(input("Enter Number : "))
c=int(input("Enter Number : "))
if a>b and a>c:
    print(a," is the greatest number")
elif b>a and b>c:
    print(b," is the greatest number")
else:
    print(c," is the greatest number")
    
#5
q=int(input("Enter Number : "))
if q>1:
    for i in range(2,q):
        if(q%i==0):
            print(q,"is not a prime number")
            print(i ,"times", q//i,"is",q)
            break
        else:
            print(q ,"is a prime number")
            break
else: 
    print(q,"is not a prime number")
    
#6
w=int(input("Enter Number : "))
p=int(input("Enter Number : "))
for j in range(w,p):
    if j>1:
        for i in range(2,j):
            if(j%i==0):
                print(j,"is not a prime number")
                print(i ,"times", j//i,"is",j)
                break
            else:
                print(j ,"is a prime number")
                break
    else: 
        print(j,"is not a prime number")
#7
h= int(input("Enter Number : "))
factorial = 1
if h<0:
    print("Sorry, factorial does not exist for negative numbers")
elif h == 0:
   print("The factorial of 0 is 1")
else:
   for i_1 in range(1,h + 1):
       factorial = factorial*i_1
   print("The factorial of",h,"is",factorial)

#8
num1= int(input("Enter Number : "))
for i_2 in range(1,11):
    print(i_2,'x',num1,'=',num1*i_2)

#9
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
            
