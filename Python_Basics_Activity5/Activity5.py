#1
def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp 
    return newList
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#2
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print(swapPositions(List, pos1-1, pos2-1))

#3
a = []
a.append("Hello")
a.append("Cognizant")
a.append(2022)
a.append("GP22MDULS001")
print("The length of list is: ", len(a))

#4
test_list = [ 1, 6, 3, 5, 3, 4 ]
print("Checking if 4 exists in list ( using in ) : ")
if 4 in test_list:
    print ("Element Exists")
    
#5
list = [7, 'Arushi', (4,2), 1]
print('List before clear:', list) 
list.clear() 
print('List after clear:',list)

#6
def Reverse(list):
    list.reverse()
    return list   
list = [10, 'training', 19, (1,2,3)]
print(Reverse(list))

#7
def sumlst(list):
    return sum(list)
list=[12,3,5,6]
sumlst(list)

#8
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
list1 = [15, 22, 31]
print(multiplyList(list1))

#9
list_1 = [10, 20, 1, 45, 99]
print("Smallest element is:", min(list_1))

#10
list_1 = [10, 20, 1, 45, 99]
print("Smallest element is:", max(list_1))

#11
def secondlarge(list):
    list.sort()
    return list[-2]
list=[4,7,8,2,3,5]
secondlarge(list)

#12
l = [1000,298,3579,100,200,-45,900]
n = 4
l.sort()
print(l)
print(l[-n:])

#13
list1 = [10, 21, 4, 45, 66, 93]
even_nos = [num for num in list1 if num % 2 == 0]
print("Even numbers in the list: ", even_nos)

#14
list1 = [12, 24, 7, 45, 62, 83]
only_odd = [num for num in list1 if num % 2 == 1]
print("Even numbers in the list: ",only_odd)

#15
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")

#16
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
    if num % 2 == 1:
        print(num, end = " ")
        
#17
list1 = [-10, 21, -4, -45, -66, 93]
num = 0  
while(num < len(list1)):
    if list1[num] >= 0:
        print(list1[num], end = " ")
    num += 1

#18
list1 = [-10, 21, -4, -45, -66, 93]
num = 0
while(num < len(list1)):
    if list1[num] <= 0:
        print(list1[num], end = " ")
    num += 1
    
#19
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
    if num >= 0:
        print(num, end = " ")
#20
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
    if num <= 0:
        print(num, end = " ")
