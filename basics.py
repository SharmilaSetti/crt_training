a=23
print(type(a))

b=23.8
print(type(b))

c=True
print(type(c))

a=8
print(bin(a))

print(31 and 20)

print(31 or 20)

li=[1,2,3,4]
li.append(5)# adding element
print(li)

li=[1,2,3,4]
li.insert(0,5) #adding elements based on index and element
print(li)

li1=[1,2,3,4]
li2=[5,6,7,8]
li1.extend(li2) #adding lists
print(li1)
print(li2)

li=[1,2,3,4] #deleting an element
li.pop()
print(li)
li.pop(0)  #deleting an element based on index value
print(li)

li=[1,2,3,4]
li.remove(3) #deleting an element based on element value
print(li)

a=("1","hello","3","4")
print(type(a))

a=("hello")
print(type(a))

a=("hello",)
print(type(a))

a=[9,44,6,2,78,23,8]
a.sort()  #ascending order
print(a)
a.sort(reverse=True) #descending order
print(a)

a=list('1234')
b=list(map(float,a))
print(a)
print(b)

t1=(4,8,8,"1234",1,23)
print(t1.count(8))
print(t1.index(23))
       
