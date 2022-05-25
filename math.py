import math

#variabls
a=int(input("plz enter a:"))
b=int(input("plz enter b:"))
c=int(input("plz enter c:"))

delta=b*b-4*a*c
if delta==0:
    x=(-b+math.sqrt(delta))
    print("moadele yek javab darad")
    print(x)
elif delta>0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("moadele 2 javab darad") 
    print(x1)
    print(x2)
elif delta<0:
    print("moadele javab nadarad")