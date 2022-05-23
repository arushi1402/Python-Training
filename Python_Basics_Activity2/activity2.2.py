
lower = 100
upper = 2000

for num in range(lower, upper + 1):
   # order of number
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)

q=int(input("Enter the number : "))
if q < 0:  
   print("Enter a positive number")  
else:
   sum=0
   while(q>0):
       sum += q
       q -=1 
print ("The sum of natural numbers are:",sum)


rows = int(input("Enter number of rows: "))
k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt:
    print(key, dt[key])
    
joke=int(input("Please enter number here : "))
print(str(joke)[::-1])
