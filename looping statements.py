#looping statements

print(list(range(1,23,8))) #range syntax--range(start,end,step_size)
"""
"""
for i in range(8,23):
    print(i,end="\n")
"""
"""
li=[1,2,3,4]
for i in li:
    print(i*i,end=" ")
"""
"""
li=[1,2,3,4,5]
k=2
for i in range(len(li)):
    if k==li[i]:
        print(i)
        break
  """
"""
li=[]
for i in range(8):
    li.append(i)
    print(li)
  """
"""
#list comprehension
li=[i*i for i in range(10)]
print(li)
li=[num for num in range(10) if num%2==0]
print(li)
"""
"""

li=[num for num in range(1,101) if num%7==0 and num%11==0]
print(li)
"""
