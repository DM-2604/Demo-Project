#Set
#syntax: var={data}
print("Set is :  Unchangeble,unindex,unduplicate")
a={1,2,3,4,4,True,"a","b"}
print("Set :",a,"\n")
#2 copy
b=a.copy()
print("copy  :",b)

#3 type
print("type ",type(a))

#4 access item in set
print("\n----------------------access item in set\n")
print(2 in a) 
print(2 not in a) 
print("We can access set element using for loop")
for i in a:
    print(i) 

#5 add or update item in set
print("\n----------------------add or update item in set\n")
a.add(52)
print("add : a.add(52)",a)

b={2,3,4,5,6,7,8,9,"t","y","i"}
a.update(b)
print("update : a.update(b)",a)


#6 remove element in set
print("\n----------------------remove element in set\n")
a.remove(5)
print("remove : a.remove(1) it will rais error when element not in set",a)

a.discard(1)
print("discard :a.discard(1) it will not raise error when elemnt not in set ",a)


p=a.pop()
print("pop : a.pop() it will remove top of set , we dont know about element which one goind to be deleting ",p)

#7 join in set
print("\n----------------------join in set") 
x={1,2,3,4,5}
y={1,2,45,56,42,23,5}
print("union: x.union(y)",x.union(y))
print("difference: x.difference(y) it retriev how many element are not in second set ",x.difference(y))
print("symmetric_difference : it retriew simple uniqe elemnt from second set",x.symmetric_difference(y))
print("x.intersection(y) : it return both set equal number" ,x.intersection(y))
q={"banana","apple"}
e={"apple"}
print(x.intersection_update(y))
