n = int(input("Enter no of digits:"))
print("enter 3 numbers:")
a=int(input())
b=int(input())
c=int(input())
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            if(i!=j and j!=k and k!=i):
                print(d[i], d[j], d[k])