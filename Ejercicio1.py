#apartado 1
t=[3,2,1,5,0,2]
for i in range (len(t)):
    for j in range(len(t)):
        if t[i]<t[j]:
            ay=t[i]
            t[i]=t[j]
            t[j]=ay
print(t)
#apartado 2
t=[3,2,1,5,0,2]
r=[]
for i in range(len(t)):
    r.append(min(t))
    t.remove(min(t))
print(r)