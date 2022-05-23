def _sum(arr): 
    sum=0
    for i in arr:
        sum = sum + i
    return(sum) 
arr=[] 
arr = [12, 3, 4, 15] 
ans = _sum(arr) 
print ('Sum of the array is ', ans) 

def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))

def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i])
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2)
printArray(arr)

def splitArr(a, n, k): 
   b = a[:k]
   return (a[k::]+b)
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n): 
    print(arr[i], end = ' ')
    
def findremainder(arr, lens, n):
    mul = 1 
    for i in range(lens):
        mul = (mul * (arr[i]))  
    return mul % n
arr = [ 100, 10, 5, 25, 35, 14 ]
lens = len(arr)
n = 11
print( findremainder(arr, lens, n))

def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
A = [6, 5, 4, 4]
print(isMonotonic(A))

import calendar
print (calendar.prcal(2023))
 