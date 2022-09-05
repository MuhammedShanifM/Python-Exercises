#Approach 1 using temp variables
mylist=[12,45,12,89]
size=len(mylist)
t=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=t
print(mylist)

#Approach 2

mylist1=[1,6,78,90]
mylist1[0],mylist1[-1]=mylist1[-1],mylist1[0]
print(mylist1)

#Approach 3 using tuple variable
mylist2=[100, 87, 34, 67, 15]
get=(mylist2[-1],mylist2[0]) #packing
mylist2[0],mylist2[-1]=get
print(mylist2)

#Approach 4 : *operand
mylist3=[12,67,89,54]
start,*middle,end=mylist3
print(start)
print(middle)
print(end)
mylist3=[end,*middle,start]
print(mylist3)

#Approach 5 using pop()

mylist4=[12,56,78,90]
first=mylist4.pop(0)
last=mylist4.pop(-1)
print(mylist4)
mylist4.insert(0,last)
mylist4.append(first)
print(mylist4)


