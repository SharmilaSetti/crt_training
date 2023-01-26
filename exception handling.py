
a=int(input("enter the num:"))
b=int(input("enter the num:"))
op=input()
if op=="+":
    print(a+b)
if op=="-":
    print(a-b)
if op=="*":
    print(a*b)
try:
    if op=="/":
        print(a/b)
    if op=="//":
        print(a//b)
    if op=="%":
        print(a%b)
except:
    print("b can't be zero")
if op=="**":
    print(a**b)
