list_1=[1,2,3,4,5]
print(list_1)

list_1=[1,2,3,4,5]
print(len(list_1))

list_1=[1,2,3,4,5]
print(list_1[0])

list_1=[1,2,3,4,5]
print(list_1[0:2])
print(list_1[0:])

list_1=[1,2,3,4,5]
for i in range(len(list_1)):
    print(list_1[i])

list_1=[1,2,3,4,5]
for i in range(len(list_1)):
    print(i,list_1[i])                       

list_1=[1,2,3,4,5]
for i in list_1:
    print(i)
    
list_1=[10,20,30,40,50]
sum=0
for i in list_1:
    sum=sum+i
    print(sum)

list_1=[10,20,30,40,50]
print("before append",list_1)
list_1.append(60)
print("after append",list_1)

list_1=[10,20,30,40,50]
list_1.append(60)
print("after append",list_1)

list_1=[10,20,30,40,50]
list_1.clear()
print("after clear",list_1)

list_1=[10,20,30,40,50]
list_2=list_1.copy()
print("after copy",list_2)

list_1=[10,10,20,20,20,30,30,10,10,10,10,10]
cnt=list_1.count(10)
print("number:",cnt)

list_1=[10,10,20,20,20,30,30,10,10,10,10,10]
count=0
for i in list_1:
    if(i==10):
        count=count+1
    else:
        count=count

list_1=[10,20,20,30,21,22,11,33,44,22,]
even_list=[]
odd_list=[]
for i in list_1:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
